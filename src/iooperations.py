from gi.repository import Gio, GLib

# import xml.etree.ElementTree as xmlet

# from .gtk.widgets.messagedialog import MessageDialog
# from .utils import update_recent_projects


def set_file_monitor(gfile: Gio.File):

    def _on_file_changed(file_monitor: Gio.FileMonitor,
                         file: Gio.File,
                         other_file: Gio.File | None,
                         event_type: Gio.FileMonitorEvent):

        if (event_type == Gio.FileMonitorEvent.Changed):
            print("file was changed, please reload")

        else:
            print("test")

    ##

    file_monitor = gfile.monitor_file(Gio.FileMonitorFlags.NONE, None)
    file_monitor.connect("changed", _on_file_changed)


def load_from_disk_async(gfile: Gio.File,
                         callback):

    def _finish_load(gfile: Gio.File,
                     result: Gio.AsyncResult):

        try:
            result, byte_content, tag = gfile.load_contents_finish(result)

        except GLib.GError as error:
            callback(None, error)

            print(str(error.message))
            return

        if not result:
            path = gfile.peek_path()
            print(f"Unable to open {path}: {byte_content}")
            return

        try:
            content = byte_content.decode('utf-8')

        except UnicodeError as err:
            path = gfile.peek_path()
            print(
                f"Unable to load the contents of {path}:"
                "the file is not encoded with UTF-8")
            return

        callback(gfile, content)

    ##

    gfile.load_contents_async(None, _finish_load)


def load_from_disk(file: Gio.File):

    result, content, etag = file.load_contents(None)

    if not result:
        path = file.peek_path()
        print(f"Unable to open {path}: {content}")
        return

    try:
        content = content.decode('utf-8')
        return content

    except UnicodeError as err:
        path = file.peek_path()
        print(
            f"Unable to load the contents of {path}:"
            "the file is not encoded with UTF-8")
        return


def scan_for_tmp():

    recovered_list = []

    # tmp_path = GLib.get_user_cache_dir()
    data_path = GLib.get_user_data_dir()
    print(data_path)

    # tmp_dir = Gio.File.new_for_path(tmp_path)
    data_dir = Gio.File.new_for_path(data_path)

    enumerator = data_dir.enumerate_children(Gio.FILE_ATTRIBUTE_STANDARD_NAME,
                                             Gio.FileQueryInfoFlags.NONE)

    '''for info in enumerator:
        file_name = info.get_name()

        if file_name.startswith("project"):

            path = tmp_path + "/" + file_name

            file = Gio.File.new_for_path(path)
            recovered_list.append(file)'''


def setup_datasets():

    data_path = GLib.get_user_data_dir()
    data_dir = Gio.File.new_for_path(data_path)
    datasets = data_dir.get_child("datasets")

    if not datasets.query_exists():
        print("não existe")
        datasets.make_directory()
    else:
        print("Existe")


def write_to_disk(file: Gio.File, content: str):  # don't work

    byte_content = GLib.Bytes.new(content.encode('utf-8'))

    size = byte_content.get_size()

    data_pointer = byte_content.get_data()

    result = file.replace_contents(data_pointer,
                                   size,
                                   None,
                                   False,
                                   Gio.FileCreateFlags.NONE)

    info = file.query_info("standard::display-name",
                           Gio.FileQueryInfoFlags.NONE)
    if info:
        display_name = info.get_attribute_string("standard::display-name")
    else:
        display_name = file.get_basename()
    if not result:
        print(f"Unable to save {display_name}")


def write_to_disk_async(gfile: Gio.File,
                        content: str,
                        callback: object):

    def finish_replace(gfile, result, data):

        try:
            result, tag = gfile.replace_contents_finish(result)

        except GLib.GError as error:
            callback(None, error)

            print(str(error.message))
            return

        info = gfile.query_info("standard::display-name",
                                Gio.FileQueryInfoFlags.NONE)

        if info:
            display_name = info.get_attribute_string(
                "standard::display-name")
        else:
            display_name = gfile.get_basename()

        if not (result):
            print(f"Unable to save {display_name}")

        else:
            callback(gfile, None)
    ##

    byte_content = GLib.Bytes.new(content.encode('utf-8'))

    gfile.replace_contents_bytes_async(byte_content,
                                       None,
                                       False,
                                       Gio.FileCreateFlags.NONE,
                                       None,
                                       finish_replace,
                                       None)


def remove_file(gfile: Gio.File):

    result = gfile.delete(None)

    print(result)
