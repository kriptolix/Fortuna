from gi.repository import Gio, GLib


def list_diretory_content(dir):
    query = Gio.FILE_ATTRIBUTE_STANDARD_NAME + \
        "," + Gio.FILE_ATTRIBUTE_STANDARD_TYPE
    enumerator = dir.enumerate_children(
        query, Gio.FileQueryInfoFlags.NONE, None)

    return enumerator


def copy_file(src, dest):
    src_file = Gio.File.new_for_path(src)
    dest_file = Gio.File.new_for_path(dest)

    src_file.copy(dest_file, Gio.FileCopyFlags.OVERWRITE, None, None)


def copy_directory_recursive(src, dest):

    def copy_recursive(parent_src, parent_dest, parent_enum):

        while True:
            try:
                info = parent_enum.next_file(None)
            except GLib.Error:
                break
            if info is None:
                break

            name = info.get_name()
            child_src = parent_src.get_child(name)
            child_dest = parent_dest.get_child(name)
            file_type = info.get_file_type()

            if file_type == Gio.FileType.DIRECTORY:
                try:
                    child_dest.make_directory_with_parents(None)
                except GLib.Error as e:
                    if e.code != Gio.io_error_exists:
                        raise e

                child_enum = child_src.enumerate_children(
                    query, Gio.FileQueryInfoFlags.NONE, None)
                copy_recursive(child_src, child_dest, child_enum)
            elif file_type == Gio.FileType.REGULAR:
                copy_file(child_src.get_path(), child_dest.get_path())

    ###

    query = Gio.FILE_ATTRIBUTE_STANDARD_NAME + \
        "," + Gio.FILE_ATTRIBUTE_STANDARD_TYPE
    enumerator = src.enumerate_children(
        query, Gio.FileQueryInfoFlags.NONE, None)

    copy_recursive(src, dest, enumerator)


def setup_datasets():

    data_user_path = GLib.get_user_data_dir()
    datasets_user_dir = Gio.File.new_for_path(
        data_user_path + "/datasets")

    if not datasets_user_dir.query_exists():

        datasets_user_dir.make_directory_with_parents(None)

        data_sys_path = GLib.get_system_data_dirs()
        datasets_sys_dir = Gio.File.new_for_path(
            data_sys_path[0] + "/fortuna/datasets")

        copy_directory_recursive(datasets_sys_dir, datasets_user_dir)


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
                        content: GLib.Bytes):

    def finish_replace(gfile, result, data):

        try:
            result, tag = gfile.replace_contents_finish(result)

        except GLib.GError as error:
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
            print(gfile)
    ##

    # byte_content = GLib.Bytes.new(content.encode('utf-8'))

    gfile.replace_contents_bytes_async(content,
                                       None,
                                       False,
                                       Gio.FileCreateFlags.NONE,
                                       None,
                                       finish_replace,
                                       None)


def remove_file(gfile: Gio.File):

    result = gfile.delete(None)

    print(result)
