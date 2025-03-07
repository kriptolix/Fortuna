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

import locale

from ...iooperations import list_diretory_content


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/Weather.ui')
class Weather(Gtk.Box):
    __gtype_name__ = 'Weather'

    _scenario = Gtk.Template.Child()
    _region = Gtk.Template.Child()
    _season = Gtk.Template.Child()
    _dramatic_mode = Gtk.Template.Child()
    _evolution = Gtk.Template.Child()
    _label = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        self._data_user_path = GLib.get_user_data_dir()

        self._scenario_model = Gtk.StringList.new()
        self._season_model = Gtk.StringList.new()
        self._region_model = Gtk.StringList.new()

        self._scenario.set_model(self._scenario_model)
        self._region.set_model(self._region_model)
        self._season.set_model(self._season_model)

        self._scenario.connect('notify::selected-item', self._item_selected)
        self._season.connect('notify::selected-item', self._item_selected)

        self._setup_scenario()
        self._setup_region()

    def _setup_scenario(self):

        scenario_dir = Gio.File.new_for_path(
            self._data_user_path + "/datasets")

        scenarios_enum = list_diretory_content(scenario_dir)

        for scenario in scenarios_enum:
            scenario_name = scenario.get_name()

            language_dir = Gio.File.new_for_path(
                self._data_user_path + "/datasets" + "/" + scenario_name)

            languages_enum = list_diretory_content(language_dir)

            for language in languages_enum:
                language_name = language.get_name()

                self._scenario_model.append(
                    scenario_name.capitalize() + " - " + language_name)

    def _setup_region(self):

        items = self._region_model.get_n_items()        

        if items > 0:

            self._region_model.splice(0, items, None)

        scenario_selected = self._scenario.get_selected_item().get_string()

        scenario = scenario_selected.replace(" - ", "/")
        scenario = scenario[0].lower() + scenario[1:]

        weather_dir = Gio.File.new_for_path(
            self._data_user_path + "/datasets/" + scenario + "/weather")

        weather_enum = list_diretory_content(weather_dir)

        for weather in weather_enum:
            weather_name = weather.get_name()

            self._region_model.append(weather_name)

    def _setup_season(self):

        items = self._season_model.get_n_items()        

        if items > 0:

            self._season_model.splice(0, items, None)

        region_selected = self._region.get_selected_item().get_string()
        region = region_selected.replace(" - ", "/")
        region = region[0].lower() + region[1:]

        scenario_selected = self._scenario.get_selected_item().get_string()
        scenario = scenario_selected.replace(" - ", "/")
        scenario = scenario[0].lower() + scenario[1:]

        season_dir = Gio.File.new_for_path(
            self._data_user_path + "/datasets/" + scenario
            + "/weather/" + region)

        season_enum = list_diretory_content(season_dir)

        for season in season_enum:
            season_name = season.get_name()

            self._season_model.append(season_name)

    def _item_selected(self, dropdown, parameter):

        if dropdown == self._scenario:
            print("scenario")
            self._setup_region()
            self._setup_season()

        if dropdown == self._region:
            print("region")
            self._setup_season()

        if dropdown == self._season:
            print("season")
