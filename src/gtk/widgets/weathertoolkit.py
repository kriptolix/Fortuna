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
from gi.repository import Gtk

from .hexagon import HexBase, HexDisplay, HexButtons
from ...utils import create_click, colors_list


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
    _description = Gtk.Template.Child()
    _severity = Gtk.Template.Child()

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

        self.status = ''       

        self._hexs_list = [
            self._00, self._01, self._02, self._03, self._04,
            self._05, self._06, self._07, self._08, self._09,
            self._10, self._11, self._12, self._13, self._14,
            self._15, self._16, self._17, self._18,
        ]

        self._colors_list = colors_list

        self._checks_list = [
            self._check_01, self._check_02, self._check_03, self._check_04,
            self._check_05, self._check_06, self._check_07, self._check_08,
        ]

        self._blockers_list = self._hex_diagram.blockers_list
        self._buttons_list = self._hex_diagram.buttons_list

        for hex in self._hexs_list:
            hex._buttons.set_visible(False)            
            create_click(hex, 1, "released", self._hex_selected, hex)

        self._image = self._hex_diagram._image       

        for button in self._buttons_list:
            button.connect("clicked", self._activate_block)

        for check in self._checks_list:
            check.connect("toggled", self._color_selected)

        self._check_01.set_active(True)
        self._hex_diagram.description.set_visible(True)
        self._hex_selected(None, None, None, None, self._00)

    def _activate_block(self, button):

        label = button.get_label()
        position = self._buttons_list.index(button)
        block = self._blockers_list[position]

        if label == "+":
            block.set_opacity(1)
            button.set_label("-")
            return

        block.set_opacity(0)
        button.set_label("+")

    def _color_selected(self, check):

        if check.get_active():

            position = self._checks_list.index(check)
            color = self._colors_list[position]

            classes = self._image.get_css_classes()

            if classes:
                for item in classes:
                    self._image.remove_css_class(item)

            self._image.add_css_class(color)

    def _hex_selected(self, gesture, npress, x, y, widget):

        for hex in self._hexs_list:
            if hex.has_css_class("hex-bg-selected"):
                hex.remove_css_class("hex-bg-selected")

        widget.add_css_class("hex-bg-selected")

    def set_status(self, status):

        if not status:
            return
        
        self._hex_diagram.description.set_text(status[0])
        self._severity.set_selected(status[1])

        self._hex_diagram.blocks_list


   
        