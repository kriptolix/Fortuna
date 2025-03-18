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

from .listobjects import KeyValuePair


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/Weather.ui')
class Weather(Gtk.Box):
    __gtype_name__ = 'Weather'

    _climate = Gtk.Template.Child()
    _description = Gtk.Template.Child()
    _biomes = Gtk.Template.Child()
    _exemples = Gtk.Template.Child()
    _dramatic_mode = Gtk.Template.Child()
    _weather_button = Gtk.Template.Child()
    _weather_label = Gtk.Template.Child()

    def __init__(self):
        super().__init__()        

        self._climate_model = Gio.ListStore(item_type=KeyValuePair)

        self._climate.set_model(self._climate_model)

        list_store_expression = Gtk.PropertyExpression.new(
            KeyValuePair, None, "value",)

        self._climate.set_expression(list_store_expression)
        self._climate.connect('notify::selected-item', self._item_selected)

        self._weather_button.connect('clicked', self._pick_weather)

    def _item_selected(self, dropdown, parameter):        
        ''

    def _pick_weather(self. button):
        ''