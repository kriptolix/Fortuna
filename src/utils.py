from gi.repository import Gtk, Gio, GLib

import time
import threading
# import yaml


def generate_yaml(season, name):

    table = {
        "season": {
            "name": '',
            "occurrences": [
            ]

        }
    }

    links = []

    for index, weather in enumerate(season):

        match index:
            case 0:
                links = [2, 3, 4, 1, 7, 18]
            case 1:
                links = [0, 4, 5, 2, 12, 15]
            case 2:
                links = [1, 5, 6, 0, 16, 11]
            case 3:
                links = [6, 7, 8, 4, 0, 17]
            case 4:
                links = [3, 8, 9, 5, 1, 0]
            case 5:
                links = [4, 9, 10, 6, 2, 1]
            case 6:
                links = [5, 10, 11, 3, 17, 2]
            case 7:
                links = [11, 0, 12, 8, 3, 16]
            case 8:
                links = [7, 12, 13, 9, 4, 8]
            case 9:
                links = [8, 13, 14, 10, 5, 4]
            case 10:
                links = [9, 14, 15, 11, 6, 5]
            case 11:
                links = [10, 15, 2, 7, 18, 6]
            case 12:
                links = [15, 1, 16, 13, 8, 7]
            case 13:
                links = [12, 16, 17, 14, 9, 8]
            case 14:
                links = [13, 17, 18, 15, 10, 9]
            case 15:
                links = [14, 18, 1, 12, 11, 10]
            case 16:
                links = [18, 2, 7, 17, 13, 12]
            case 17:
                links = [16, 6, 3, 18, 14, 13]
            case 18:
                links = [17, 11, 0, 16, 15, 14]

        evolutions = []

        for id, link in enumerate(links):

            if (id + 1) == weather[2] | weather[3] | weather[4]:
                evolutions.append(weather[0])

            evolutions.append(season[link][0])

        occurrence = {
            'occurrence': {
                'name': weather[0],
                'severity': weather[1],
                'evolutions': evolutions
            }
        }

        table["season"]["occurrences"].append(occurrence)

    table["season"]["name"] = "verão"
    # yaml_data = yaml.dump(table, default_flow_style=False, allow_unicode=True)

    # print(yaml_data)


summer = [
    ["Chuva", 0, 0, 0, 0],
    ["Garoa morna", 0, 0, 0, 0],
    ["Tempo quente e abafado", 1, 0, 0, 5],
    ["Chuva forte", 1, 0, 0, 1],
    ["Sereno morno", 0, 0, 0, 0],
    ["Nublado e quente", 0, 0, 0, 0],
    ["Quente e com vento", 1, 0, 0, 4],
    ["Chuva torrencial!", 2, 0, 0, 1],
    ["Nublado e humido", 0, 0, 0, 0],
    ["Agradavelmente morno", 0, 0, 0, 0],
    ["Quente e seco", 1, 0, 0, 0],
    ["Seco,com ondas de calor", 2, 0, 0, 4],
    ["Tempestade!", 2, 0, 0, 1],
    ["Nublado e com vento", 0, 0, 0, 0],
    ["Brisa morna", 0, 0, 0, 0],
    ["Tempo ensolarado e claro", 0, 0, 0, 4],
    ["Vento forte!", 1, 0, 0, 2],
    ["parcialmente nublado e ameno", 0, 0, 0, 0],
    ["tempo limpo e ameno", 0, 0, 0, 0],
]

spring = [
    ["garoa fria", 0, 0, 0, 0],
    ["quente e humido", 0, 0, 0, 6],
    ["quente e seco", 1, 0, 0, 5],
    ["chuva leve", 0, 0, 0, 1],
    ["umido e ameno", 1, 0, 0, 5],
    ["nublado e quente", 0, 0, 0, 0],
    ["ar cheio de polem", 1, 0, 4, 5],
    ["chuva forte", 1, 0, 0, 1],
    ["granizo pequeno", 1, 0, 0, 1],
    ["tempo claro e ameno", 1, 0, 0, 0],
    ["ensolarado e claro", 1, 0, 0, 0],
    ["agradavelmente morno", 1, 0, 0, 4],
    ["chuva com neve", 1, 0, 0, 0],
    ["chuva de granizo", 1, 0, 0, 0],
    ["nevoa fria", 1, 0, 0, 0],
    ["frio e seco", 0, 0, 0, 3],
    ["nevando e com vento", 0, 0, 0, 2],
    ["nevando forte", 0, 0, 0, 2],
    ["nevando leve", 0, 0, 0, 1]
]

winter = [
    ["frio e claro", 0, 0, 0, 0],
    ["chuva de granizo", 1, 0, 0, 0],
    ["nevasca", 2, 0, 0, 5],
    ["nublado e ameno", 0, 0, 0, 0],
    ["claro e com vento", 0, 0, 0, 0],
    ["chuva com neve", 1, 0, 0, 0],
    ["nevando e com vento", 1, 0, 0, 0],
    ["ensolarado e ameno", 0, 0, 0, 0],
    ["nevoa fria", 0, 0, 0, 0],
    ["frio e humido", 0, 0, 0, 0],
    ["chuva com neve", 1, 0, 0, 0],
    ["nevando leve", 1, 0, 0, 4],
    ["garoa leve", 0, 0, 0, 0],
    ["sereno frio", 1, 0, 0, 0],
    ["nublado e frio", 0, 0, 0, 0],
    ["chuva de granizo", 0, 0, 0, 0],
    ["chuva forte", 1, 0, 0, 2],
    ["ventos gelados", 0, 0, 0, 0],
    ["nublado e congelante", 0, 0, 0, 0],
]

autumn = [
    ["ensolarado e ameno", 0, 0, 0, 1],
    ["garoa", 0, 0, 0, 0],
    ["tempestade", 2, 0, 0, 4],
    ["agradavelmente morno", 0, 0, 0, 0],
    ["parcialmente nublado", 0, 0, 0, 0],
    ["rajadas de chuva e vento", 1, 0, 0, 0],
    ["chuva pesada", 1, 0, 0, 0],
    "ventos esporadicos!",
    "neblina fria",

    "ensolarado e claro",
    "nublado e congelante",
    "ventos frios",
    "ensolarado e ameno",
    "nublado e ameno",
    "nublado e humido",
    "nevoa densa!",
    "garoa",
    "chuva e vento",
    "chuva e neblina!",
    "limpo e com vento",
    "tempestade!"
]

weather = [
    "agradável"
    "ameno e úmido"
    "brisa quente"
    "chuva"
    "chuva de granizo!"
    "chuva e neblina!"
    "chuva e vento"
    "chuva forte!"
    "chuva fria!"
    "chuva forte"
    "chuva torrencial!"
    "claro e ameno"
    "claro e com vento"
    "ensolarado e ameno"
    "ensolarado e claro"
    "frio e úmido"
    "frio e claro"
    "frio e seco"
    "garoa"
    "garoa leve"
    "garoa morna"
    "gelado e nublado"
    "limpo e com vento"
    "neblina fria"
    "nevando forte!"
    "nevando leve"
    "nevasca!!"
    "nevoa densa!"
    "nublado e morno"
    "nublado e ameno"
    "nublado e com vento"
    "nublado e congelante"
    "nublado e frio"
    "nublado e úmido"
    "ondas de calor!!"
    "parcialmente nublado e ameno"
    "quente e abafado!"
    "quente e com vento!"
    "quente e úmido"
    "quente e seco!"
    "quente nublado"
    "sereno"
    "tempestade!"
    "tempeporal!"
    "tempo limpo e ameno"
    "vento e neve!"
    "vento forte!"
    "vento frio"
    "ventos esporádicos!"
    "ventos frios"
    "sereno morno"
]

generate_yaml(summer, "verão")

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


def update_recent_projects(settings, path):
    """
    Update the recent accessed project files list from homepage.

    Parameters
    ----------
    settings : Gio.Settings
        Retrieving application settings.
    path : str
        Accessed project file path.            
    """

    recent_projects = settings.get_strv("recent-projects")

    if (path in recent_projects):
        recent_projects.remove(path)

    recent_projects.insert(0, path)

    if (len(recent_projects) >= 4):
        recent_projects.pop()

    settings.set_strv("recent-projects", recent_projects)


class SaveCountdown():
    """
    A class used to controll the time interval for autosave 

    ...

    Attributes
    ----------
    method : function
        a function to be called when time is triged    
    seconds : int
        The number seconds of a pause that trigger countdow (default is 3)
    current_seconds : int
        Hold the current time of timer
    timer : threading.Thread
        Threading Thread tha holds the timer coundown
    stop_timer : threading.Event
        Threading event tha represents timer stop    
    reset_timer : threading.Event
        Threading event tha represents timer reset

    Methods
    -------
    countdown()
        Prints the animals name and what sound it makes
    update_count()
    """

    def __init__(self, seconds, method):
        """
        Parameters
        ----------
        method : function
            a function to be called when time is triged       
        seconds : int, optional
            The number seconds of a pause that trigger countdow (default is 3)
        """

        self.method = method
        self.seconds = seconds
        self.current_seconds = seconds
        self.timer = threading.Thread(target=self._countdown)
        self.timer.daemon = True
        self.stop_timer = threading.Event()
        self.reset_timer = threading.Event()

    def _countdown(self):
        """
        Create a timer on that calls a function when get to zero
        """

        while not self.stop_timer.is_set():
            while self.current_seconds > 0 and not self.reset_timer.is_set():
                time.sleep(1)
                self.current_seconds -= 1

            if self.current_seconds == 0:
                print("tmp saved")
                self.method()

            self.reset_timer.wait()
            self.current_seconds = self.seconds
            self.reset_timer.clear()

    def update_count(self):
        """
        If timer is not active, start it. If timer is active reset it to
        maximum value
        """

        if not self.timer.is_alive():
            self.timer.start()
        else:
            self.reset_timer.set()
