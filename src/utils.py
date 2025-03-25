from gi.repository import Gtk, Gio, Adw

# p1 esquerda, p4 direta
vertical = [
    [0, 1, 2],
    [3, 4, 5, 6],
    [7, 8, 9, 10, 11],
    [12, 13, 14, 15],
    [16, 17, 18]
]

# p6 esquerda, p3 direta
left = [
    [7, 12, 16],
    [3, 8, 13, 17],
    [0, 4, 9, 14, 18],
    [1, 5, 10, 15],
    [2, 6, 11]
]

# p5 esquerda, p2 direita
right = [
    [0, 3, 7],
    [1, 4, 8, 12],
    [2, 5, 9, 13, 16],
    [6, 10, 14, 17],
    [11, 15, 18]
]

colors_list = [
    "color-rain-1", "color-rain-2", "color-cold-1", "color-cold-2",
    "color-cold-3", "color-nippy-1", "color-warm-1", "color-warm-2",
]


def clone_state(hex_ori, hex_dst):

    hex_dst._description = hex_ori._description
    hex_dst._set_severity(hex_ori._severity)

    for index, block in enumerate(hex_ori.blockers_list):
        hex_dst.blockers_list[index].set_opacity(block.get_opacity())

    hex_dst._set_color(hex_ori._color)


def create_action(action_group, prefix, name, callback,
                  shortcuts=None, parameter=None, target=None):
    """
    Add an action to an action group.

    Parameters
    ----------
    action_group : Gio.SimpleActionGroup
        Where the actions is added
    prefix : str 
        Prefix used to actions on action group
    name : str 
        The name of the action.
    callback : function)
        The function to be called when the action is
        activated.
    shortcuts : list, optional
        An optional list of strings representing accelerators.
    parameter : GLib.VariantType, optional
        Possibles parameters for the action.
    target : any, optional 
        A standard value to action parameter.
    """

    action = Gio.SimpleAction.new(name, parameter)
    action.connect("activate", callback)
    action_group.add_action(action)
    detailed_name = f"{prefix}.{name}"

    if (target):
        detailed_name = f"{prefix}.{name}::{target}"

    if shortcuts:
        action_group.set_accels_for_action(detailed_name, shortcuts)


def create_click(widget, btn_nunber, trigger, callback, data=None):
    """
    Add an click action to a widget.

    Parameters
    ----------
    widget : Gtk.Widget
        Where the actions is added.
    btn_nunber : int
        Mouse button number that will activate de action.
    trigger : str
        Button behavior that will trigget the action.
    callback : function
        The function to be called when the action is
        activated.
    data : any, optional
        Data to pass to callback.
    """

    click = Gtk.GestureClick.new()
    click.set_button(btn_nunber)
    click.connect(trigger, callback, data)

    widget.add_controller(click)


def setup_animation(start, end, widget, property):

    target_property = Adw.PropertyAnimationTarget.new(widget,
                                                      property)

    animation_timed = Adw.TimedAnimation.new(widget,
                                             start,
                                             end,
                                             550,
                                             target_property)

    animation_timed.set_easing(6)
    return animation_timed
