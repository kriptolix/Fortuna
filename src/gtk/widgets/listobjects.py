from gi.repository import GObject


class KeyValuePair(GObject.Object):

    key = GObject.Property(
        type=str, flags=GObject.ParamFlags.READWRITE, default="")

    value = GObject.Property(
        type=str,
        nick="Value",
        blurb="Value",
        flags=GObject.ParamFlags.READWRITE,
        default="",
    )

    def __init__(self, key, value):
        super().__init__()

        self.key = key
        self.value = value
