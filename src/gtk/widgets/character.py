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
from gi.repository import Gtk, Gio, GLib, GObject

import os
# import yaml

from .listobjects import KeyValuePair

@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/Character.ui')
class Character(Gtk.Box):
    __gtype_name__ = 'Character'

    _scenario = Gtk.Template.Child()
    _region = Gtk.Template.Child()
    # _season = Gtk.Template.Child()
    # _dramatic_mode = Gtk.Template.Child()
    _generate = Gtk.Template.Child()
    _label = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        self._data_user_path = GLib.get_user_data_dir()

        self._scenario_model = Gio.ListStore(item_type=KeyValuePair)
        self._season_model = Gio.ListStore(item_type=KeyValuePair)
        self._region_model = Gio.ListStore(item_type=KeyValuePair)

        self._scenario.set_model(self._scenario_model)
        self._region.set_model(self._region_model)
        # self._season.set_model(self._season_model)

        list_store_expression = Gtk.PropertyExpression.new(
            KeyValuePair, None, "value",)

        self._scenario.set_expression(list_store_expression)
        self._region.set_expression(list_store_expression)
        # self._season.set_expression(list_store_expression)        

        self._scenario.connect('notify::selected-item', self._item_selected)
        self._region.connect('notify::selected-item', self._item_selected)
        # self._season.connect('notify::selected-item', self._item_selected)

    def _item_selected(self, dropdown, parameter):

        if dropdown == self._scenario:
            self._setup_region()

        if dropdown == self._region:
            self._setup_season()

        if dropdown == self._season:
            self._load_season()

    def _setup_season(self):

        scenario = self._scenario.get_selected_item().key
        region = self._region.get_selected_item().key

        season = Gio.File.new_for_path(self._data_user_path
                                       + "/datasets/" + scenario
                                       + "/weather/" + region)

        self._setup_dropdown(season, self._season_model)

    def _setup_region(self):

        scenario = self._scenario.get_selected_item().key

        weather_dir = Gio.File.new_for_path(
            self._data_user_path + "/datasets/" + scenario + "/weather")

        self._setup_dropdown(weather_dir,
                             self._region_model)

    def _setup_scenario(self):

        scenario_dir = Gio.File.new_for_path(
            self._data_user_path + "/datasets")

        self._setup_dropdown(scenario_dir,
                             self._scenario_model)

    def _setup_dropdown(self, gdirectory, model):

        items = model.get_n_items()

        if items > 0:
            model.remove_all()

        content_enum = 'list_diretory_content(gdirectory)'

        for content in content_enum:

            content_name = content.get_name()
            value = content_name.capitalize().replace("_", " ")

            if content.get_file_type() == Gio.FileType.REGULAR:
                tmp_value = os.path.splitext(content_name)
                value = tmp_value[0].capitalize().replace("_", " ")

            pair = KeyValuePair(key=content_name, value=value)

            model.append(pair)

    def _load_season(self):

        scenario = self._scenario.get_selected_item().key
        region = self._region.get_selected_item().key
        season = self._season.get_selected_item().key

        season = Gio.File.new_for_path(self._data_user_path
                                       + "/datasets/" + scenario
                                       + "/weather/" + region
                                       + "/" + season)

        if not season.query_exists():
            print("directory: ", season.get_path())
            return

        # file = load_from_disk(season)
        # season_obj = yaml.safe_load(file)

        # print(season_obj)
