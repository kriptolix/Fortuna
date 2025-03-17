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

from ...utils import colors_list


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


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/HexDisplay.ui')
class HexDisplay(Gtk.Box):
    __gtype_name__ = 'HexDisplay'

    _top_right = Gtk.Template.Child()
    _bottom_right = Gtk.Template.Child()
    _top_side = Gtk.Template.Child()
    _bottom_side = Gtk.Template.Child()
    _top_left = Gtk.Template.Child()
    _bottom_left = Gtk.Template.Child()
    _description = Gtk.Template.Child()
    _severity = Gtk.Template.Child()

    def __init__(self):
        super().__init__()


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/HexBase.ui')
class HexBase(Gtk.Box):
    __gtype_name__ = 'HexBase'

    _image = Gtk.Template.Child()
    _display = Gtk.Template.Child()
    _buttons = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        self._severity = 0
        self._description = self._display._description
        self._color = 0

        self._blockers_list = [
            self._display._top_side, self._display._top_right,
            self._display._bottom_right, self._display._bottom_side,
            self._display._bottom_left, self._display._top_left
        ]

        self.buttons_list = [
            self._buttons._top_side, self._buttons._top_right,
            self._buttons._bottom_right, self._buttons._bottom_side,
            self._buttons._bottom_left, self._buttons._top_left
        ]

    def _set_severity(self, severity):

        match severity:
            case 0:
                self._display._severity.set_visible(False)
                self._severity = 0
            case 1:
                self._display._severity.set_visible(True)
                self._severity = 1
                if self._display._severity.has_css_class("error"):
                    self._display._severity.remove_css_class("error")
                    # self._display._severity.add_css_class("warning")

            case 2:
                self._display._severity.set_visible(True)
                self._severity = 2
                self._display._severity.add_css_class("error")
                
                '''
                if self._display._severity.has_css_class("warning"):
                    self._display._severity.remove_css_class("warning")
                    self._display._severity.add_css_class("error")
                '''

    def _set_color(self, color):

        css_classes = self._image.get_css_classes()

        if css_classes:
            for css in css_classes:
                if css in colors_list:
                    self._image.remove_css_class(css)

        self._image.add_css_class(colors_list[color])
        self._color = color

    def _set_text(self, text):
        self._description.set_text(text)

    def _set_block(self, position, value):

        block = self._blockers_list[position]
        block.set_opacity(value)

    def _get_text(self):
        text = self._description.get_text()
        return text
