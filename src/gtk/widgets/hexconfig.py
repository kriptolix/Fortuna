# HexConfig.py
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

from .hexagon import HexBase, HexBlocks, HexButtons


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/HexConfig.ui')
class HexConfig(Gtk.Box):
    __gtype_name__ = 'HexConfig'

    _hexbase = Gtk.Template.Child()
    _severity = Gtk.Template.Child()
    _description = Gtk.Template.Child()
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

        self._blocks = HexBlocks()
        self._buttons = HexButtons()

        self._image = self._hexbase._image

        self._hexbase._upper_layer.add_overlay(self._blocks)
        self._hexbase._under_layer.add_overlay(self._buttons)

        self._checks_list = [
            self._check_01,
            self._check_02,
            self._check_03,
            self._check_04,
            self._check_05,
            self._check_06,
            self._check_07,
            self._check_08,
        ]

        self._colors_list = [
            "color-rain-1",
            "color-rain-2",
            "color-cold-1",
            "color-cold-2",
            "color-cold-3",
            "color-nippy-1",
            "color-warm-1",
            "color-warm-2",
        ]

        self._blocks_list = [
            self._blocks._top_right,
            self._blocks._bottom_right,
            self._blocks._top_side,
            self._blocks._bottom_side,
            self._blocks._top_left,
            self._blocks._bottom_left
        ]

        self._buttons_list = [
            self._buttons._top_right,
            self._buttons._bottom_right,
            self._buttons._top_side,
            self._buttons._bottom_side,
            self._buttons._top_left,
            self._buttons._bottom_left
        ]

        for button in self._buttons_list:
            button.connect("clicked", self._activate_block)

        for check in self._checks_list:
            check.connect("toggled", self._color_selected)

        self._check_01.set_active(True)

    def _activate_block(self, button):

        label = button.get_label()
        position = self._buttons_list.index(button)
        block = self._blocks_list[position]

        if label == "+":
            block.set_opacity(1)
            button.set_label("-")
            return

        block.set_opacity(0)
        button.set_label("+")

    def _color_selected(self, check):

        print("color selected")

        if check.get_active():

            position = self._checks_list.index(check)
            color = self._colors_list[position]

            classes = self._image.get_css_classes()

            if classes:
                for item in classes:
                    self._image.remove_css_class(item)

            self._image.add_css_class(color)

    def _set_hex_text(self):
        ''
