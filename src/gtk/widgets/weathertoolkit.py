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
from gi.repository import Gtk, GObject, Gdk

import csv

from .hexagon import HexBase, HexDisplay, HexButtons
from ...utils import create_click
from ...datasets.strings import weather_names_list


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
    _text_combo = Gtk.Template.Child()
    _danger_combo = Gtk.Template.Child()
    _export_button = Gtk.Template.Child()
    _used_label = Gtk.Template.Child()

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
        self._drag_coords = [0, 0]

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

        weather_model = Gtk.StringList.new(weather_names_list)
        severity_model = Gtk.StringList.new(["Unharmful",
                                             "Dangerous",
                                             "Disastrous"])

        self._text_combo.set_model(weather_model)
        self._danger_combo.set_model(severity_model)

        self._image = self._hex_diagram._image

        for hex in self._hexs_list:
            hex._buttons.set_visible(False)
            create_click(hex, 1, "released", self._on_hex_selected, hex)
            hex.drag_source.connect("drag-begin", self._on_drag_begin, hex)
            hex.drag_source.connect("prepare", self._on_prepare, hex)

            # Update row visuals during DnD operation
            hex.drop_controller.connect("enter", self._on_drop_hover)
            hex.drop_controller.connect("leave", self._on_drop_hover)
            hex.drop_controller.connect("motion", self._on_drop_hover)

            hex.drop_target.connect("drop", self._on_drop, hex)

        for button in self._hex_diagram.buttons_list:
            button.connect("clicked", self._on_activate_block)

        for check in self._checks_list:
            check.connect("toggled", self._on_color_selected)

        self._danger_combo.connect('notify::selected-item',
                                   self._on_severity_selected)

        self._text_combo.connect('notify::selected-item',
                                 self._on_text_selected)

        self._export_button.connect("clicked", self._serialize_flower)

        self._on_hex_selected(None, None, None, None, self._00)
        self._text_combo.set_selected(Gtk.INVALID_LIST_POSITION)

    def _on_text_selected(self, dropdown, parameter):

        position = self._text_combo.get_selected()
        self._used_label.set_opacity(0)

        for hex in self._hexs_list:
            if position == hex._text_ref:
                self._used_label.set_opacity(1)

        self._hex_diagram._set_text(position)
        self._hex_selected._set_text(position)

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

        severity = self._danger_combo.get_selected()
        self._hex_diagram._set_severity(severity)
        self._hex_selected._set_severity(severity)

    def _on_hex_selected(self, gesture, npress, x, y, widget):

        for hex in self._hexs_list:
            if hex.has_css_class("hex-bg-selected"):
                hex.remove_css_class("hex-bg-selected")

        widget.add_css_class("hex-bg-selected")

        self._hex_selected = widget
        self._clone_state(self._hex_selected, self._hex_diagram)
        self._update_hex_config()

    def _clone_state(self, ori_hex, dst_hex):

        text_ref = ori_hex._text_ref
        dst_hex._set_text(text_ref)

        severity = ori_hex._severity
        dst_hex._set_severity(severity)

        for index, block in enumerate(ori_hex._blockers_list):
            dst_hex._blockers_list[index].set_opacity(
                block.get_opacity())

        dst_hex._set_color(ori_hex._color)

    def _update_hex_config(self):

        text_ref = self._hex_diagram._text_ref
        severity = self._hex_diagram._severity
        color_check = self._hex_diagram._color

        if not text_ref:
            text_ref = Gtk.INVALID_LIST_POSITION

        self._text_combo.set_selected(text_ref)
        self._danger_combo.set_selected(severity)

        check = self._checks_list[color_check]
        check.set_active(True)

    def _serialize_flower(self, button):

        serialized = []

        for hex in self._hexs_list:
            row = [hex._get_text_ref(),
                   hex._severity,
                   hex._color,
                   ]

            for block in hex._blockers_list:
                row.append(int(block.get_opacity()))

            serialized.append(row)

        print(serialized)

    def _list_to_csv(self, season, csv_file):

        csv_writer = csv.writer(csv_file)
        for item in season:
            csv_writer.writerow(item)

    def _csv_to_list(self, csv_file):
        season = []

        csv_reader = csv.reader(csv_file)
        for linha in csv_reader:
            # Converte os 8 últimos itens para inteiros
            item = [linha[0]] + list(map(int, linha[1:]))
            season.append(item)
        return season

    def _on_prepare(self, source, x, y, hexagon):

        self._drag_coords[0] = x
        self._drag_coords[1] = y

        value = GObject.Value()
        value.init(HexBase)
        value.set_object(hexagon)

        return Gdk.ContentProvider.new_for_value(value)

    def _on_drag_begin(self, _source, drag_object, hexagon):

        drag_widget = HexBase()

        self._clone_state(hexagon, drag_widget)

        icon = Gtk.DragIcon.get_for_drag(drag_object)
        icon.set_child(drag_widget)

        drag_object.set_hotspot(self._drag_coords[0], self._drag_coords[1])

    def _on_drop_hover(self,
                       controller: Gtk.DropControllerMotion,
                       x: int | None = None,
                       y: int | None = None,) -> None:

        hexagon = controller.get_widget()

        if (x and y):

            hexagon.add_css_class("hex-bg-selected")
            return

        hexagon.remove_css_class("hex-bg-selected")

    def _on_drop(self, _drop, drag_target, x, y, drop_target):

        if (not drag_target or not drop_target
                or drag_target == drop_target):

            return False

        cache_hex = HexBase()
        self._clone_state(drop_target, cache_hex)
        self._clone_state(drag_target, drop_target)
        self._clone_state(cache_hex, drag_target)
