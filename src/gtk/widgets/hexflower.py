# HexFlower.py
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

from .hexagon import HexBase, HexBlocks, HexText


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/HexFlower.ui')
class HexFlower(Gtk.Box):
    __gtype_name__ = 'HexFlower'

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

    def __init__(self):
        super().__init__()        

        self._hexs_list = [
            self._00,
            self._01,
            self._02,
            self._03,
            self._04,
            self._05,
            self._06,
            self._07,
            self._08,
            self._09,
            self._10,
            self._11,
            self._12,
            self._13,
            self._14,
            self._15,
            self._16,
            self._17,
            self._18,
        ]

        for hex in self._hexs_list:
            blocks = HexBlocks()
            text = HexText()
            hex._upper_layer.add_overlay(text)
            hex._under_layer.add_overlay(blocks)

