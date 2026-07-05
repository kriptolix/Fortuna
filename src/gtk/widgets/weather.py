# Weather.py
#
# Copyright 2025 k
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk, Gio, GLib

import os
import random
import yaml

from ...datasets.strings import climate_names_list, season_tips
from ...utils import setup_animation

from ...utils import vertical, left, right

_MOVE_DIRECTIONS = {
    1: (vertical, -1),
    2: (right, +1),
    3: (left, +1),
    4: (vertical, +1),
    5: (right, -1),
    6: (left, -1),
}


def _move_index(index, groups, step):
    for group in groups:
        if index in group:
            pos = group.index(index) + step
            if pos < 0:
                pos = len(group) - 1
            elif pos > len(group) - 1:
                pos = 0
            return group[pos]
    raise ValueError(f"índice {index} não encontrado nos grupos")


MAPS_DIR = os.path.join("/app/share/fortuna/src", "datasets", "generic_ptBR", "weather")


def _slugify(climate_name):
    return (climate_name.lower()
            .replace(":", "")
            .replace(",", "")
            .replace(" ", "_"))


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/Weather.ui')
class Weather(Gtk.Box):
    __gtype_name__ = 'Weather'

    _climate_combo = Gtk.Template.Child()
    _dramatic_mode = Gtk.Template.Child()
    _info_icon = Gtk.Template.Child()
    _weather_button = Gtk.Template.Child()
    _weather_label = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        self._selected_climate = None   # lista de 19 "occurrence" (dict)
        self._actual_index = None       # índice físico (0-18) atual
        self._actual_weather = None     # dict "occurrence" atual

        self._text = ''

        climate_model = Gtk.StringList.new(climate_names_list)

        self._climate_combo.set_model(climate_model)

        self._climate_combo.connect('notify::selected-item',
                                    self._item_selected)

        self._weather_button.connect('clicked', self._pick_weather)
       
        self._climate_combo.set_selected(0)

    def _load_climate(self, climate_name):
        
        filename = os.path.join(MAPS_DIR, f"{_slugify(climate_name)}.yaml")

        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except (OSError, yaml.YAMLError) as error:
            print(f"Não foi possível carregar o mapa '{filename}': {error}")
            return None

        return [item["occurrence"] for item in data["season"]["occurrences"]]

    def _item_selected(self, dropdown, parameter):

        position = self._climate_combo.get_selected()

        if position == Gtk.INVALID_LIST_POSITION:
            return

        climate_name = climate_names_list[position]

        occurrences = self._load_climate(climate_name)
        if occurrences is not None:
            self._selected_climate = occurrences
      
        self._actual_index = None
        self._actual_weather = None
        
        tips = season_tips[position] if position < len(season_tips) else None
        if tips:
            self._info_icon.set_tooltip_text('\n\n'.join(tips))

    def _pick_weather(self, button):

        if not self._selected_climate:
            print("Nenhum mapa climático carregado.")
            return

        if self._actual_index is None:
            self._actual_index = random.randrange(len(self._selected_climate))
            self._actual_weather = self._selected_climate[self._actual_index]
            self._text = self._actual_weather["name"]
            self._fade_out()
            return

        chances_weights = [1, 1, 1, 2, 2, 2, 2]
        move = random.choices([1, 2, 3, 4, 5, 6, 7], chances_weights)[0]

        print("Move: ", move)

        evolutions = self._actual_weather["evolutions"]
        current_name = self._actual_weather["name"]

        if move == 7:
            # Permanecer: nada muda.
            self._text = current_name
            self._fade_out()
            return

        next_name = evolutions[move]

        if next_name == current_name:
            # Direção bloqueada (ou coincidentemente igual): equivalente
            # ao antigo "blocked" - não muda de hexágono nem de clima.
            if self._dramatic_mode.get_active():
                print("retry")
                self._pick_weather(None)
                return

            print("blocked")
            self._text = current_name
            self._fade_out()
            return

        groups, step = _MOVE_DIRECTIONS[move]
        self._actual_index = _move_index(self._actual_index, groups, step)
        self._actual_weather = self._selected_climate[self._actual_index]
        self._text = self._actual_weather["name"]

        self._fade_out()

    def _fade_out(self):
        self._hide = setup_animation(1, 0, self._weather_label, "opacity")

        self._hide.connect("done", self._animation_end)

        self._weather_button.set_sensitive(False)
        self._hide.play()

    def _fade_in(self):
        self._show = setup_animation(0, 1, self._weather_label, "opacity")

        self._show.connect("done", self._animation_end)

        self._show.play()

    def _animation_end(self, animation):

        if animation == self._hide:
            self._weather_label.set_text(self._text)
            self._fade_in()
            return

        self._weather_button.set_sensitive(True)
        self._weather_button.grab_focus()