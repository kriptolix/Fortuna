# Cycles.py
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
from gi.repository import Gtk, Gdk

import os
import random
import yaml

from ...datasets.strings import climate_names_list, season_tips
from ...utils import setup_animation

# NOTA: os pesos abaixo duplicam EVOLUTION_WEIGHTS de weathertoolkit.py.
# Se for possível, vale mover essa constante para utils.py para manter
# uma única fonte de verdade entre o editor e o consumo em jogo.
EVOLUTION_WEIGHTS = {
    "none": 0,
    "rare": 1,
    "normal": 10,
    "high": 20,
}


MAPS_DIR = os.path.join("/app/share/fortuna/src", "datasets", "generic_ptBR", "weather")
IMG_DIR = os.path.join("/app/share", "images")


def _slugify(climate_name):
    return (climate_name.lower()
            .replace(":", "")
            .replace(",", "")
            .replace(" ", "_"))


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/Cycles.ui')
class Cycles(Gtk.Box):
    __gtype_name__ = 'Cycles'
    
    _weather_combo = Gtk.Template.Child()
    _seasons_combo = Gtk.Template.Child()    
    _weather_button = Gtk.Template.Child()
    _moon_button = Gtk.Template.Child()
    _weather_label = Gtk.Template.Child()
    _background = Gtk.Template.Child()
    

    def __init__(self):
        super().__init__()

        self._selected_climate = None   # lista de 19 "occurrence" (dict)
        self._actual_index = None       # índice físico (0-18) atual
        self._actual_weather = None     # dict "occurrence" atual

        self._text = ''

        climate_model = Gtk.StringList.new(climate_names_list)

        self._weather_combo.set_model(climate_model)

        self._weather_combo.connect('notify::selected-item',
                                    self._item_selected)

        self._weather_button.connect('clicked', self._pick_weather)
       
        self._weather_combo.set_selected(0)

        self._item_selected(self._weather_combo, None)

        self._background.set_content_fit(Gtk.ContentFit.CONTAIN)
        self._background.set_can_shrink(True)

        filename = os.path.join(IMG_DIR, "storm2.png")

        storm = Gdk.Texture.new_from_filename(filename)
        self._background.set_paintable(storm)

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

        position = self._weather_combo.get_selected()

        if position == Gtk.INVALID_LIST_POSITION:
            return

        climate_name = climate_names_list[position]

        occurrences = self._load_climate(climate_name)
        if occurrences is not None:
            self._selected_climate = occurrences
      
        self._actual_index = None
        self._actual_weather = None
        
        '''
        tips = season_tips[position] if position < len(season_tips) else None
        if tips:
            self._info_icon.set_tooltip_text('\n\n'.join(tips))
        '''

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

        current_name = self._actual_weather["name"]
        evolutions = self._actual_weather.get("evolutions", [])

        # evolutions[0] é "permanecer"; evolutions[1:7] são as 6
        # direções do hexflower. O peso de cada uma vem do YAML
        # ("none"/"rare"/"normal"/"high"), já resolvido pelo editor
        # (inclusive pulando vizinhos vazios).
        weights = [
            EVOLUTION_WEIGHTS.get(evo.get("weight"), 0)
            if isinstance(evo, dict) else 0
            for evo in evolutions
        ]

        if not evolutions or not any(weights):
            # Sem evoluções cadastradas, ou todas com peso zero
            # (bloqueadas): permanece no estado atual.
            self._text = current_name
            self._fade_out()
            return

        chosen = random.choices(range(len(evolutions)), weights=weights)[0]
        chosen_evo = evolutions[chosen]
        next_name = chosen_evo.get("name") if isinstance(chosen_evo, dict) \
            else None

        if not next_name or next_name == current_name:
            # Permanecer no estado atual - seja porque a posição 0
            # ("permanecer") foi sorteada, seja porque a direção
            # sorteada aponta para o mesmo fenômeno (vizinho ausente ou
            # coincidentemente igual).
            if chosen != 0 and self._dramatic_mode.get_active():
                print("retry")
                self._pick_weather(None)
                return

            self._text = current_name
            self._fade_out()
            return

        candidates = [i for i, occ in enumerate(self._selected_climate)
                     if occ.get("name") == next_name]

        if not candidates:
            # Fenômeno referenciado na evolução não existe (mais) no
            # mapa carregado - mantém o estado atual e avisa.
            print(f"Aviso: fenômeno '{next_name}' não encontrado no mapa "
                  "carregado; permanecendo no estado atual.")
            self._text = current_name
            self._fade_out()
            return

        # Se mais de um hexágono do mapa tiver o mesmo fenômeno, escolhe
        # um deles aleatoriamente entre os candidatos.
        self._actual_index = random.choice(candidates)
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