# Weathertoolkit.py
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
from gi.repository import Gtk, GObject

from .hexagon import HexBase, HexDisplay, HexButtons
from ...utils import create_click


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/WeatherToolkit.ui')
class WeatherToolkit(Gtk.Box):
    __gtype_name__ = 'WeatherToolkit'

    _00 = Gtk.Template.Child()
    _01 = Gtk.Template.Child()
    _02 = Gtk.Template.Child()
    _03 = Gtk.Template.Child()
    _04 = Gtk.Template.Child()
    _05 = Gtk.Template.Child()
    _06 = Gtk.Template.Child()
    _07 = Gtk.Template.Child()
    _08 = Gtk.Template.Child()
    _09 = Gtk.Template.Child()
    _10 = Gtk.Template.Child()
    _11 = Gtk.Template.Child()
    _12 = Gtk.Template.Child()
    _13 = Gtk.Template.Child()
    _14 = Gtk.Template.Child()
    _15 = Gtk.Template.Child()
    _16 = Gtk.Template.Child()
    _17 = Gtk.Template.Child()
    _18 = Gtk.Template.Child()

    _hex_diagram = Gtk.Template.Child()
    _text_entry = Gtk.Template.Child()
    _danger_box = Gtk.Template.Child()

    _check_01 = Gtk.Template.Child()
    _check_02 = Gtk.Template.Child()
    _check_03 = Gtk.Template.Child()
    _check_04 = Gtk.Template.Child()
    _check_05 = Gtk.Template.Child()
    _check_06 = Gtk.Template.Child()
    _check_07 = Gtk.Template.Child()
    _check_08 = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        self._hex_selected = None

        self._hexs_list = [
            self._00, self._01, self._02, self._03, self._04,
            self._05, self._06, self._07, self._08, self._09,
            self._10, self._11, self._12, self._13, self._14,
            self._15, self._16, self._17, self._18,
        ]

        self._checks_list = [
            self._check_01, self._check_02, self._check_03, self._check_04,
            self._check_05, self._check_06, self._check_07, self._check_08,
        ]

        self._image = self._hex_diagram._image

        for hex in self._hexs_list:
            hex._buttons.set_visible(False)
            create_click(hex, 1, "released", self._on_hex_selected, hex)

        for button in self._hex_diagram.buttons_list:
            button.connect("clicked", self._on_activate_block)

        for check in self._checks_list:
            check.connect("toggled", self._on_color_selected)

        self._danger_box.connect('notify::selected-item',
                                 self._on_severity_selected)

        self._insert = self._text_entry.connect("insert-text",
                                                self._on_change_text)

        self._delete = self._text_entry.connect("delete-text",
                                                self._on_change_text)
        self._change = self._text_entry.connect("changed",
                                                self._on_change_text)

        self._on_hex_selected(None, None, None, None, self._00)

    def _on_change_text(self, *args):

        text = self._text_entry.get_text()

        self._hex_diagram._set_text(text)
        self._hex_selected._set_text(text)

    def _on_activate_block(self, button):

        label = button.get_label()
        position = self._hex_diagram.buttons_list.index(button)

        if label == "+":
            self._hex_diagram._set_block(position, 1)
            self._hex_selected._set_block(position, 1)
            button.set_label("-")
            return

        self._hex_diagram._set_block(position, 0)
        self._hex_selected._set_block(position, 0)
        button.set_label("+")

    def _on_color_selected(self, check):

        if check.get_active():

            position = self._checks_list.index(check)
            self._hex_diagram._set_color(position)
            self._hex_selected._set_color(position)

    def _on_severity_selected(self, dropdown, parameter):

        severity = self._danger_box.get_selected()
        self._hex_diagram._set_severity(severity)
        self._hex_selected._set_severity(severity)

    def _on_hex_selected(self, gesture, npress, x, y, widget):

        for hex in self._hexs_list:
            if hex.has_css_class("hex-bg-selected"):
                hex.remove_css_class("hex-bg-selected")

        widget.add_css_class("hex-bg-selected")

        self._hex_selected = widget
        self._clone_state()

    def _clone_state(self):

        text = self._hex_selected._get_text()

        self._hex_diagram._set_text(text)
        GObject.signal_handler_disconnect(self._text_entry,  self._insert)
        self._text_entry.set_text(text)
        self._insert = self._text_entry.connect("insert-text",
                                                self._on_change_text)

        severity = self._hex_selected._severity

        self._hex_diagram._set_severity(severity)
        self._danger_box.set_selected(severity)

        for index, block in enumerate(self._hex_selected._blockers_list):
            self._hex_diagram._blockers_list[index].set_opacity(
                block.get_opacity())

        self._hex_diagram._set_color(self._hex_selected._color)
        position = self._hex_selected._color

        check = self._checks_list[position]
        check.set_active(True)
