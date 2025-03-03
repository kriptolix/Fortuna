# Weather.py
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

import locale

from .hexagon import Hexagon


@Gtk.Template(resource_path='/io/github/kriptolix/Fortuna'
              '/src/gtk/ui/Weather.ui')
class Weather(Gtk.Box):
    __gtype_name__ = 'Weather'

    _region = Gtk.Template.Child()
    _season = Gtk.Template.Child()
    _dramatic_mode = Gtk.Template.Child()
    _evolution = Gtk.Template.Child()
    _label = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        locale.setlocale(locale.LC_ALL, "")
        language = locale.getlocale(locale.LC_MESSAGES)[0]

        # checkar se ha tradução, se nao, mostrar em ingles
        
        
