# mainwindow.py
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
from gi.repository import Gtk, Gdk, GObject

from .weather import Weather
from .oracle import Oracle
from .character import Character


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/MainWindow.ui')
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    _stack = Gtk.Template.Child()
    _toggle_t_weather = Gtk.Template.Child()
    _toggle_b_weather = Gtk.Template.Child()
    _toggle_t_oracle = Gtk.Template.Child()
    _toggle_b_oracle = Gtk.Template.Child()
    _toggle_t_character = Gtk.Template.Child()
    _toggle_b_character = Gtk.Template.Child()
    _oracle = Gtk.Template.Child()
    _weather = Gtk.Template.Child()
    _character = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_resource('/io/github/kriptolix/'
                                        'Fortuna/data/fortuna.css')
        add_provider = Gtk.StyleContext.add_provider_for_display
        add_provider(Gdk.Display.get_default(),
                     css_provider,
                     Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        toggles = [
            [self._toggle_t_weather, self._toggle_b_weather],
            [self._toggle_t_character, self._toggle_b_character],
            [self._toggle_t_oracle, self._toggle_b_oracle]
        ]

        flags = GObject.BindingFlags.SYNC_CREATE | GObject.BindingFlags.BIDIRECTIONAL

        for toggle in toggles:
            toggle[0].connect("toggled", self._toggle_page)

            toggle[0].bind_property("active",
                                    toggle[1],
                                    "active",
                                    flags)

    def _toggle_page(self, toggle):

        if (toggle == (self._toggle_t_weather or self._toggle_b_weather)
                and toggle.get_active()):
            self._stack.set_visible_child(self._weather)

        if (toggle == (self._toggle_t_character or self._toggle_t_character)
                and toggle.get_active()):
            self._stack.set_visible_child(self._character)

        if (toggle == (self._toggle_t_oracle or self._toggle_t_oracle)
                and toggle.get_active()):
            self._stack.set_visible_child(self._oracle)
