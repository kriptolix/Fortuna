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

    _hexagon = Gtk.Template.Child()
    _severity = Gtk.Template.Child()
    _description = Gtk.Template.Child()    

    def __init__(self):
        super().__init__()

        self._blocks = HexBlocks()
        self._buttons = HexButtons()

        self._hexagon._under_layer.add_overlay(self._blocks)
        self._hexagon._upper_layer.add_overlay(self._buttons)

        self._buttons_list = [
            self._blocks._top_right,
            self._blocks._bottom_right,
            self._blocks._top_side,
            self._blocks._bottom_side,
            self._blocks._top_left,
            self._blocks._bottom_left
        ]

        self._blocks_list = [
            self._buttons._top_right,
            self._buttons._bottom_right,
            self._buttons._top_side,
            self._buttons._bottom_side,
            self._buttons._top_left,
            self._buttons._bottom_left
        ]

        for button in self._blocks_list:
            button.connect("clicked", self._activate_block)

    def _activate_block(self, button):

        label = button.get_label()
        position = self._blocks_list.index(button)
        block = self._blocks_list[position]

        if label == "+":
            block.set_opacity(1)
            button.set_label("-")
            return

        block.set_opacity(0)
        button.set_label("+")

    def _set_hex_text(self):
        ''
