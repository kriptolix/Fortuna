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
from gi.repository import Gtk, Gio

import os
import random

from ...datasets.strings import semi_arid_dry, weather_names_list
from ...datasets.strings import climate_names_list, season_tips
from ...utils import setup_animation, vertical, right, left


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

        self._selected_climate = semi_arid_dry
        self._actual_weather = None

        self._text = ''

        climate_model = Gtk.StringList.new(climate_names_list)

        self._climate_combo.set_model(climate_model)

        self._climate_combo.connect('notify::selected-item',
                                    self._item_selected)

        self._weather_button.connect('clicked', self._pick_weather)

    def _item_selected(self, dropdown, parameter):
        
        tooltip = (season_tips[0][0] + '\n\n'
                   + season_tips[0][1] + '\n\n'
                   + season_tips[0][2])

        self._info_icon.set_tooltip_text(tooltip)        

    def _pick_weather(self, button):

        if not self._actual_weather:
            self._actual_weather = random.choice(self._selected_climate)
            self._text = weather_names_list[self._actual_weather[0]]
            self._fade_out()
            return

        chances_wigths = [1, 1, 1, 2, 2, 2, 2]

        move = random.choices([1, 2, 3, 4, 5, 6, 7],
                              chances_wigths)

        print("Move: ", move[0])
        # print(self._actual_weather)

        blockers = self._actual_weather[3:]

        print(blockers)

        for index, element in enumerate(blockers):
            if element == 1:
                if index + 1 == move[0] or move == 7:
                    if self._dramatic_mode.get_active():
                        self._pick_weather(None)
                        print("retry")
                        return
                    print("blocked")
                    self._fade_out()
                    return

        match move[0]:
            case 1:
                self._make_move(-1, vertical)
            case 4:
                self._make_move(1, vertical)
            case 5:
                self._make_move(-1, right)
            case 2:
                self._make_move(1, right)
            case 6:
                self._make_move(-1, left)
            case 3:
                self._make_move(1, left)

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

    def _make_move(self, route, groups):

        index = self._selected_climate.index(self._actual_weather)

        # print("index: ", index)

        for group in groups:
            if index in group:

                position = group.index(index)

                print(group, position, route)

                next_pos = position + route

                if next_pos < 0:
                    next_pos = len(group) - 1

                if next_pos > len(group) - 1:
                    next_pos = 0

                next_ref = group[next_pos]

                next_elem = self._selected_climate[next_ref]
                self._text = weather_names_list[next_elem[0]]
                self._actual_weather = next_elem

                # print(self._text)
                # print(next_elem)
