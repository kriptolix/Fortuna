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


from gi.repository import Gtk, GObject, Gdk, Gio, GLib

import csv
import yaml

from .hexagon import HexBase, HexDisplay, HexButtons
from ...utils import create_click, take_screeshot, write_to_disk_async
from ...datasets.strings import weather_names_list, semi_arid_dry

# ADJACENCY: mapa index (0-18) -> lista de 6 índices vizinhos, na ordem
# fixa [Superior, Superior-direita, Inferior-direita, Inferior,
# Inferior-esquerda, Superior-esquerda] (índice 1 = topo, sentido horário).
# Essa ordem bate exatamente com hex._blockers_list em hexagon.py:
#   [top_side, top_right, bottom_right, bottom_side, bottom_left, top_left]
# Construída diretamente a partir de utils.vertical/left/right (validado
# batendo com os pesos padrão da especificação: move "vertical,-1" pesa 1
# e corresponde a "Superior", etc. - ver comentário completo em weather.py).
from ...utils import vertical, left, right

EVOLUTION_WEIGHTS = {
            "none": 0,
            "rare": 1,
            "normal": 10,
            "high": 20,
        }

_DIRECTIONS = [
    ("Superior", vertical, -1),
    ("Superior direita", right, +1),
    ("Inferior direita", left, +1),
    ("Inferior", vertical, +1),
    ("Inferior esquerda", right, -1),
    ("Superior esquerda", left, -1),
]

DIRECTION_LABELS = [name for name, _, _ in _DIRECTIONS]


def _move_index(index, groups, step):
    for group in groups:
        if index in group:
            pos = group.index(index) + step
            if pos < 0:
                pos = len(group) - 1
            elif pos > len(group) - 1:
                pos = 0
            return group[pos]
    raise ValueError(f"índice {index} não encontrado nos grupos")


ADJACENCY = {
    i: [_move_index(i, groups, step) for _, groups, step in _DIRECTIONS]
    for i in range(19)
}


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
    _hex_box = Gtk.Template.Child()
    _text_combo = Gtk.Template.Child()
    _danger_combo = Gtk.Template.Child()
    _export_button = Gtk.Template.Child()
    _import_button = Gtk.Template.Child()
    _save_button = Gtk.Template.Child()
    _used_label = Gtk.Template.Child()
    _file = Gtk.Template.Child()

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
        self._import_button.connect("clicked", self._deserialize_flower)
        self._save_button.connect("clicked", self._save_screenshot)

        self._on_hex_selected(None, None, None, None, self._00)
        self._text_combo.set_selected(Gtk.INVALID_LIST_POSITION)

    def _on_text_selected(self, dropdown, parameter):
 
        position = self._text_combo.get_selected()
        self._used_label.set_opacity(0)
 
        for hex in self._hexs_list:
            if hex is self._hex_selected:
                # o próprio hexágono selecionado já tem esse texto (é o
                # valor atual dele) - não conta como "em uso" por outro.
                continue
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

    def _build_season_dict(self, season_name):
        """Monta o YAML final expandindo os relacionamentos do hexflower.

        As chances padrão vêm da geometria do hexflower.
        Exceções de transição:
            normal  -> usa peso geométrico
            rare    -> usa peso raro
            blocked -> peso zero
        """        

        names_by_idx = {}
        for index, hex in enumerate(self._hexs_list):
            names_by_idx[index] = weather_names_list[hex._get_text_ref()]

        occurrences = []

        for index, hex in enumerate(self._hexs_list):
            name = names_by_idx[index]

            evolutions = []

            # Permanecer no estado atual.
            # A posição 0 representa estabilidade do clima.
            evolutions.append({
                "name": name,
                "weight": self._get_stay_weight(index)
            })

            # Evoluções para os 6 vizinhos
            for dir_pos, n_idx in enumerate(ADJACENCY[index]):

                neighbor_name = names_by_idx[n_idx]

                relation = hex._relations_list[dir_pos]
                # relation esperado:
                # "normal", "rare" ou "blocked"

                if relation == "blocked":
                    weight = "blocked"

                elif relation == "rare":
                    weight = "rare"

                else:
                    if dir_pos in [0, 1, 2]:
                        weight = "normal"
                    else:
                        weight = "high"

                evolutions.append({
                    "name": neighbor_name,
                    "weight": weight
                })

            occurrences.append({
                "occurrence": {
                    "name": name,
                    "severity": hex._severity,
                    "color": hex._color,
                    "evolutions": evolutions,
                }
            })

        return {
            "season": {
                "name": season_name,
                "occurrences": occurrences
            }
        }

    def _serialize_flower(self, button):

        def when_writed(gfile, error):
            if error:
                print(str(error.message))

        def _choose_dialog_callback(file_dialog: Gtk.FileDialog,
                                    task: Gio.AsyncResult,
                                    data=None):
            try:
                gfile = file_dialog.save_finish(task)
            except GLib.GError as error:
                print(str(error.message))
                return

            season_name = gfile.get_basename()
            if season_name.lower().endswith((".yaml", ".yml")):
                season_name = season_name.rsplit(".", 1)[0]

            season_dict = self._build_season_dict(season_name)
            yaml_text = yaml.dump(season_dict, allow_unicode=True,
                                  sort_keys=False,
                                  default_flow_style=False)

            self.last_loaded_file = gfile
            write_to_disk_async(gfile,
                                GLib.Bytes.new(yaml_text.encode("utf-8")),
                                when_writed)

        file_dialog = Gtk.FileDialog.new()
        file_dialog.set_title("Exportar Mapa (YAML)")
        file_dialog.set_initial_name("mapa.yaml")
        file_dialog.save(None, None, _choose_dialog_callback)

    def _apply_season_dict(self, season_dict):
        """Aplica um dict no formato season/occurrences aos 19 hexágonos.
        A ordem das occurrences deve corresponder à numeração 0-18 da
        especificação."""

        occurrences = season_dict["season"]["occurrences"]

        for index, item in enumerate(occurrences):
            occ = item["occurrence"]
            hex = self._hexs_list[index]

            try:
                text_ref = weather_names_list.index(occ["name"])
            except ValueError:
                # Fenômeno não encontrado em weather_names_list - mantém
                # o hexágono como está e avisa no console para revisão
                # manual.
                print(f"Aviso: fenômeno '{occ['name']}' não encontrado em "
                      "weather_names_list (hexágono "
                      f"{index} não foi atualizado).")
                continue

            hex._set_text(text_ref)
            hex._set_severity(occ["severity"])
            hex._set_color(occ.get("color", 0))

            # Bloqueios: reconstruídos comparando cada entrada de
            # 'evolutions' com o próprio nome do fenômeno (uma evolução
            # igual ao nome do hexágono, fora a posição 0/"permanecer",
            # indica bloqueio nessa direção).
            evolutions = occ.get("evolutions", [])
            for dir_pos, block_widget in enumerate(hex._blockers_list):
                evo_pos = dir_pos + 1  # posição 0 é "permanecer"
                is_blocked = (evo_pos < len(evolutions)
                             and evolutions[evo_pos] == occ["name"])
                block_widget.set_opacity(1 if is_blocked else 0)

    def _deserialize_flower(self, button):

        def _choose_dialog_callback(file_dialog: Gtk.FileDialog,
                                    task: Gio.AsyncResult,
                                    data=None):
            try:
                gfile = file_dialog.open_finish(task)
            except GLib.GError as error:
                print(str(error.message))
                return

            try:
                ok, contents, _etag = gfile.load_contents(None)
            except GLib.GError as error:
                print(str(error.message))
                return

            if not ok:
                print("Falha ao ler o arquivo selecionado.")
                return

            try:
                season_dict = yaml.safe_load(contents.decode("utf-8"))
            except yaml.YAMLError as error:
                print(f"Arquivo YAML inválido: {error}")
                return

            self._apply_season_dict(season_dict)

        file_dialog = Gtk.FileDialog.new()
        file_dialog.set_title("Importar Mapa (YAML)")
        file_dialog.open(None, None, _choose_dialog_callback)

    # --- Métodos legados (CSV) mantidos apenas para referência; não são
    # mais usados pelos botões de exportar/importar, que agora usam YAML.
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

    def _save_screenshot(self, button):

        def when_writed(gfile, error):

            if (error):
                print(str(error.message))
                return

        def _choose_dialog_callback(file_dialog: Gtk.FileDialog,
                                    task: Gio.AsyncResult,
                                    data: bytes):

            try:
                gfile = file_dialog.save_finish(task)

            except GLib.GError as error:

                print(str(error.message))
                return

            self.last_loaded_file = gfile
            write_to_disk_async(gfile, data, when_writed)

        ##

        for hex in self._hexs_list:
            if hex.has_css_class("hex-bg-selected"):
                hex.remove_css_class("hex-bg-selected")        

        screenshot = take_screeshot(self._hex_box)

        self._hex_selected.add_css_class("hex-bg-selected")

        file_dialog = Gtk.FileDialog.new()
        file_dialog.set_title("Export File")
        file_dialog.save(None, None,
                         _choose_dialog_callback,
                         screenshot)