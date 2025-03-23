# Oracle.py
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
from gi.repository import Gtk, Gio

import random

from ...utils import setup_animation

@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/Oracle.ui')
class Oracle(Gtk.Box):
    __gtype_name__ = 'Oracle'

    _chances_combo = Gtk.Template.Child()
    _ask_button = Gtk.Template.Child()
    _answer_label = Gtk.Template.Child()

    def __init__(self):
        super().__init__()        

        self._answers_list = [
            _("Strongly No"),
            _("No"),
            _("No but.."),
            _("Yes but..."),
            _("Yes"),
            _("Strongly Yes"),
        ]

        self._chances_list = [
            _("Terrible"),
            _("Bad"),
            _("Regular"),
            _("God"),
            _("Great"),
        ]

        self._chances_wigths = [
            [5, 10, 5, 3, 2, 1],
            [5, 5, 10, 3, 2, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 2, 3, 5, 10, 5],
            [1, 2, 3, 5, 5, 10],
        ]

        self._chances_model = Gtk.StringList.new()

        for chance in self._chances_list:
            self._chances_model.append(chance)

        self._chances_combo.set_model(self._chances_model)
        self._chances_combo.set_selected(2)

        self._ask_button.connect("clicked", self._question_asked)

    def _question_asked(self, button):

        selected = self._chances_combo.get_selected()

        result = random.choices(self._answers_list,
                                self._chances_wigths[selected])

        self._text = result[0]
        self._fade_out()    

    def _fade_out(self):
        self._hide = setup_animation(1, 0, self._answer_label, "opacity")

        self._hide.connect("done", self._animation_end)

        self._ask_button.set_sensitive(False)
        self._hide.play()

    def _fade_in(self):
        self._show = setup_animation(0, 1, self._answer_label, "opacity")

        self._show.connect("done", self._animation_end)

        self._show.play()

    def _animation_end(self, animation):

        if animation == self._hide:
            self._answer_label.set_text(self._text)
            self._fade_in()
            return

        self._ask_button.set_sensitive(True)
