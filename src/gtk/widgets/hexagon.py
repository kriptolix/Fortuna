# hexagon.py
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
              '/src/gtk/ui/Hexagon.ui')
class Hexagon(Gtk.Box):
    __gtype_name__ = 'Hexagon'

    _label = Gtk.Template.Child()
    _entry = Gtk.Template.Child()
    _top_center = Gtk.Template.Child()
    _stack = Gtk.Template.Child()
    _severity = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        self.left_click = Gtk.GestureClick.new()
        self.left_click.set_button(1)
        self.left_click.connect("released", self._on_left_click)
        self._label.add_controller(self.left_click)

        self.motion = Gtk.EventControllerMotion.new()
        self.motion.connect("enter", self._on_overmouse)
        self.motion.connect("leave", self._on_overmouse)

        self.add_controller(self.motion)

        self._entry.connect("activate", self._activate_entry)

    def _on_left_click(self, *args) -> None:

        content = self._label.get_text()

        if content:
            self._entry.set_text(content)

        if self._stack.set_visible_child != self._entry:
            self._stack.set_visible_child(self._entry)
            self._entry.set_editable(True)

    def _activate_entry(self, *args):
        print("enter")
        content = self._entry.get_text()
        self._label.set_text(content)
        self._stack.set_visible_child(self._label)
        self._entry.set_editable(False)

    def _on_overmouse(self, widget, x=None, y=None):

        if x and y:
            self._severity.set_opacity(1)
            return

        self._severity.set_opacity(0)
