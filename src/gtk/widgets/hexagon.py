# Hexagon.py
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


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/HexButtons.ui')
class HexButtons(Gtk.Box):
    __gtype_name__ = 'HexButtons'

    _top_right = Gtk.Template.Child()
    _bottom_right = Gtk.Template.Child()
    _top_side = Gtk.Template.Child()
    _bottom_side = Gtk.Template.Child()
    _top_left = Gtk.Template.Child()
    _bottom_left = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        self.motion = Gtk.EventControllerMotion.new()
        self.motion.connect("enter", self._on_overmouse)
        self.motion.connect("leave", self._on_overmouse)

        self.add_controller(self.motion)

    def _on_overmouse(self, widget, x=None, y=None):

        if x and y:
            self._severity.set_opacity(1)
            return

        self._severity.set_opacity(0)


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/HexBlocks.ui')
class HexBlocks(Gtk.Box):
    __gtype_name__ = 'HexBlocks'

    _top_right = Gtk.Template.Child()
    _bottom_right = Gtk.Template.Child()
    _top_side = Gtk.Template.Child()
    _bottom_side = Gtk.Template.Child()
    _top_left = Gtk.Template.Child()
    _bottom_left = Gtk.Template.Child()

    def __init__(self):
        super().__init__()


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/HexBase.ui')
class HexBase(Gtk.Box):
    __gtype_name__ = 'HexBase'

    _image = Gtk.Template.Child()
    _upper_layer = Gtk.Template.Child()
    _under_layer = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
