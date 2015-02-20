# -*- coding: utf-8 -*-
from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.layout import floating
from subprocess import Popen, check_output, PIPE, STDOUT
from time import sleep
from os import path
import re
import shlex


################################### SCREENS ####################################

class Theme(object):
    bar = dict(
         opacity=0.9,
         background='131a13'
         )

    class Layout(object):
        border_args = dict(
            border_normal='#000000',
            border_focus='#550000',
            border_width=2,
        )

    class Widget(object):
        icons_path = path.expandvars('$HOME/.config/qtile/icons/')
        default = dict(
                padding=1,
                fontsize=14,
                font='DejaVu Sans',
                foreground='5CCCCC'
                )
        group_box = dict(default, **dict(
                other_screen_border='880000',
                padding=3,
                urgent_alert_method='text',
                fontsize=12,
                ))
        window_name = dict(default, **dict())
        backlight = dict(default, **dict(
            backlight_name='intel_backlight'))
        volume = dict(default, **dict(
            theme_path=icons_path
        ))
        battery_icon = dict(default, **dict(
            theme_path=icons_path,
            battery_name='BAT1'
        ))
        battery = dict(default, **dict(
                padding=0,
                battery_name='BAT1',
                charge_char='',
                discharge_char='',
                energy_now_file='charge_now',
                energy_full_file='charge_full',
                power_now_file='current_now',
                update_delay=4
                ))
        # yahoo_weather = dict(default.items() + dict(
        #        location='Madrid, SP'
        #        ).items())
        clock = dict(default, **dict(
            fmt='%A %d %b | %H:%M',  # '%a, %d de %b, %H:%M',
            fontsize=14,
            padding=10
        ))
        current_layout = dict(default, **dict(
            fontsize=12,
            foreground='7070ff'
            ))

################################### SCREENS ####################################

screens = [
    Screen(
        top = bar.Bar([
            widget.GroupBox(**Theme.Widget.group_box),
            widget.Sep(padding=10),
            widget.CurrentLayout(**Theme.Widget.current_layout),
            widget.Sep(padding=10),
            widget.Prompt(**Theme.Widget.default),
            widget.WindowName(**Theme.Widget.window_name),
            #widget.TaskList(),
            #       widget.Mpris(),
            widget.Backlight(**Theme.Widget.backlight),
            widget.Volume(**Theme.Widget.volume),
            widget.Sep(padding=10),
            widget.BatteryIcon(**Theme.Widget.battery_icon),
            widget.Battery(**Theme.Widget.battery),
            widget.Sep(padding=10),
            widget.Systray(),
            widget.Clock(**Theme.Widget.clock),
            #widget.Notify(foreground='#ffff00')
        ], 22, **Theme.bar)),
    Screen(top = bar.Bar(
        [
            widget.GroupBox(**Theme.Widget.group_box),
            widget.Sep(padding=10),
            widget.CurrentLayout(**Theme.Widget.current_layout),
            widget.WindowName(**Theme.Widget.window_name),
            widget.Clock(**Theme.Widget.clock),
        ], 22, **Theme.bar)
       ),
]

############################# KEYBOARD BINDINGS ################################

mod = "mod4"
alt = "mod1"
shift = "shift"
ctrl = "control"

TERMINAL = "sakura"
EDITOR = "emacsclient -ca \"\""
BROWSER = "firefox"
FILEMANAGER = "pcmanfm"
WALLPAPER = path.expandvars("$HOME/.wallpaper")
LOCKIMAGE = path.expandvars("$HOME/.wallpaper-lock")
LOCKER = 'i3lock'

keys = [

    Key([shift, alt], "q", lazy.shutdown()),
    Key([mod, shift], "r", lazy.restart()),
    Key([mod, shift], "x", lazy.window.kill()),

    #Key([mod], "r", lazy.spawncmd()),
    Key([mod], "r", lazy.spawn("gmrun &")),
    Key([mod], "g", lazy.switchgroup()),

    Key([mod], "Return", lazy.spawn(TERMINAL)),
    Key([mod, shift], "Return", lazy.spawn(EDITOR)),

    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),  # Stack, xmonad-tall
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),  # Stack, xmonad-tall
    Key([mod], "Tab", lazy.layout.next()),
    Key([mod,shift], "Tab", lazy.layout.previous()),
    Key([mod], "p", lazy.layout.previous()),
    Key([mod], "n", lazy.layout.next()),
    Key([mod, shift], "f", lazy.window.toggle_floating()),
    Key([mod, shift], "m", lazy.window.toggle_maximized()),

    Key([mod], "space", lazy.nextlayout()),
    Key([mod,shift], "space", lazy.prevlayout()),

    Key([mod], "Left", lazy.group.prevgroup()),
    Key([mod], "Right", lazy.group.nextgroup()),

    #Key([mod,shift], "Left", lazy.to_next_screen()),
    #Key([mod,shift], "Right", lazy.to_prev_screen()),
    Key([mod], "o", lazy.to_next_screen()),
    #Key([mod,shift], "Right", lazy.to_prev_screen()),

    Key([mod, shift], "space", lazy.layout.rotate()),
    Key([mod, shift], "minus", lazy.layout.toggle_split()),

    # start specific apps
    Key([mod], "F1",              lazy.spawn(BROWSER)),
    Key([mod], "F2",              lazy.spawn(FILEMANAGER)),
    Key([mod], "F3",              lazy.spawn("spotify")),
#    Key([mod], "F4",              lazy.spawn("psi")),

    # Change the volume if your keyboard has special volume keys.
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulseaudio-ctl up")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulseaudio-ctl down")),
    Key([], "XF86AudioMute", lazy.spawn("pulseaudio-ctl mute")),
    Key([], 'XF86Calculator', lazy.spawn('xcalc')),
    # win + calc => lock screen now
    Key([mod], "l", lazy.spawn("xautolock -locknow")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    #Key([], "XF86TouchpadToggle",   lazy.spawn("synclient TouchpadOff=$(synclient -l | grep -c 'TouchpadOff.*=.*0')")),
    Key([], 'XF86Mail', lazy.spawn('%s "http://mail.google.com"' % BROWSER)),
    #Key([], 'XF86HomePage', lazy.to_screen(0), lazy.group["code"].toscreen()),
]

############################## MOUSE BINDINGS ##################################

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

##################################  GROUPS  ####################################

# groups = [
#     ("1", Group("Terminal")),
#     ("2", Group("Emacs")),
#     ("3", Group("Browser")),
#     ("4", Group("Irc")),
#     ("5", Group("Talk")),
#     ("6", Group("Music")),
#     ("7", Group("Files")),
#     ("8", Group("Other")),
# ]
groups = [
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
    Group("8"),
]
for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(Key([mod, shift], i.name, lazy.window.togroup(i.name)))


##################################  LAYOUTS  ###################################

layouts = [
    layout.MonadTall(**Theme.Layout.border_args),
    layout.Tile(**Theme.Layout.border_args),
    layout.Stack(stacks=2, **Theme.Layout.border_args),
    layout.Max(),
    layout.TreeTab(),  # display tree windows on left
#   layout.RatioTile(),
]

# setting default auto flot types and float rules
floating_layout = layout.Floating(
    auto_float_types = floating.DEFAULT_FLOAT_WM_TYPES,
    float_rules = [dict(wmclass="pinentry"),            #emacs pass window
                   dict(wmclass="Calculator"),          #Gnome Calculator
                   dict(wmclass="Ediff"),               #emacs diff window
                   dict(wname="Unlock Login Keyring")])

# make dialog floating
@hook.subscribe.client_new
def floating_dialogs(window):
    if(window.window.get_wm_type() == 'dialog' or window.window.get_wm_transient_for()):
        window.floating = True

    try:
        wm_class = window.window.get_wm_class() or []
        if ("gmrun" in wm_class
                or "feh" in wm_class
                or "keepass2" in wm_class
                or "crx_gclkcflnjahgejhappicbhcpllkpakej" in wm_class
                or "xcaliber-gui.tcl" in wm_class
                or "gksu" in wm_class
                or "xcalc" in wm_class
                or "wmshutdown" in wm_class
                or "thunar" in wm_class
                or "soffice" in wm_class
                ):
            window.floating = True

    except Exception as e:
        with open('/tmp/logfile', 'a') as logfile:
            logfile.write(''.join(['\n', str(e)]))
            return

def is_running(process):
    s = Popen(["ps", "axuw"], stdout=PIPE)
    for x in s.stdout:
        if re.search(process.encode(), x):
            return True
    return False


def execute_once(command):    
    process = shlex.split(command)
    if process and not is_running(process[0]):
        return Popen(process)

def cmd_get(process):
    return check_output("%s; exit 0;" % process, stderr=STDOUT, shell=True)

def get_num_screens():
    return int(cmd_get("xrandr|grep -c \ connected"))    

def get_screens():
    lines = (line for line in cmd_get("xrandr | grep -A 1 \ connected").splitlines() if line != "--")
    screens = {}
    got_primary = False
    for screen, resolution in zip(lines, lines):
        scr = screen.split()[0]
        screens[scr] = {
            "resolution": resolution.split()[0],
            "screen": scr,
        }
        # first screen not being the laptop one gets to be the primary
        if not got_primary and not scr.startswith(b"LVDS"):
            screens[scr]["primary"] = True
            got_primary = True
    return screens

def gen_screen_line(screen, resolution=None, position=None, primary=None):
    s = "--output {screen} ".format(screen=screen)
    if resolution:
        s += "--mode {resolution} --rotate normal ".format(resolution=resolution)
        if position:
            s += "--pos {position} ".format(position=position)
        if primary:
            s += "--primary "
    else:
        s += " --off "
    return s

def gen_xrand():
    modes = []
    screen_port=["LVDS", "HDMI", "VGA", "DP"]
    active_screens = get_screens()
    for port in screen_port:
        screen_name = "%s1" % port
        screen = (active_screens.get(screen_name, None) or 
                  {"screen": screen_name})
        modes.append(gen_screen_line(**screen))

    return "xrandr " + " ".join(modes)

def setup_screens():
    execute_once(gen_xrand())

    # if len(screens) == 1:
    #     execute_once("xrandr " +
    #     "--output HDMI1 --off " +
    #     "--output LVDS1 --mode 1366x768 --pos 0x0 --rotate normal " +
    #     "--output DP1 --off " +
    #     "--output VGA1 --off")
    # else:
    #     execute_once("xbacklight -set 100")
    #     if bool(int(cmd_get("xrandr|grep -c \"VGA[0-9]* connected\""))):
    #         execute_once("xrandr --output HDMI1 --off " + 
    #                      "--output LVDS1 --mode 1366x768 --pos 0x232 --rotate normal " +
    #                      "--output DP1 --off " +
    #                      "--output VGA1 --primary --mode 1920x1080")

    #         # execute_once("xrandr " +
    #         # "--output HDMI1 --off " +
    #         # "--output DP1 --off " +
    #         # "--output VGA1 --primary --mode 1920x1080 --rotate normal --right-of " +
    #         # "--output LVDS1 --mode 1366x768 --pos 0x0 --rotate normal --pos 277x1080")
    #     elif bool(int(cmd_get("xrandr|grep -c \"HDMI[0-9]* connected\""))):
    #         execute_once("xrandr --output VGA1 --off " + 
    #                      "--output LVDS1 --mode 1366x768 --pos 0x232 --rotate normal " +
    #                      "--output DP1 --off " +
    #                      "--output HDMI1 --primary --mode 1920x1080")
    #         # execute_once("xrandr " +
    #         # "--output VGA1 --off " +
    #         # "--output DP1 --off " +
    #         # "--output HDMI1 --primary --mode 1920x1080 --rotate normal --right-of " +
    #         # "--output LVDS1 --mode 1366x768 --pos 0x0 --rotate normal --pos 1920x312")
    #     else:
    #         execute_once("xrandr " +
    #         "--output HDMI1 --off " +
    #         "--output LVDS1 --mode 1366x768 --pos 0x0 --rotate normal " +
    #         "--output DP1 --off " +
    #         "--output VGA1 --off")

def gen_locker(time=5):
    lockerstring = LOCKER
    if LOCKIMAGE and path.exists(LOCKIMAGE):
        lockerstring += " -i %s -t" % LOCKIMAGE
    else:
        lockerstring += " -c 131a13"
    return "xautolock -time %s -locker '%s'" % (time, lockerstring)

def update_wallpaper(image_path):
    if path.exists(image_path):
        execute_once("feh  --bg-scale %s" % image_path)
    # TODO: log error

@hook.subscribe.startup
def startup():
    execute_once("xbacklight -set 40")
    execute_once("xcompmgr")
    execute_once("nm-applet")
    #execute_once("xcaliber --bR=256 --bG=256 --bB=200 --gR=1.0 --gG=1.0 --gB=0.85")
    execute_once("dunst")
    execute_once(gen_locker())
    #execute_once("nice -n 19 dropbox start")
    execute_once("nice -n 19 xrdb -merge %s" % path.expandvars("$HOME/.Xresources"))
    setup_screens()
    update_wallpaper(WALLPAPER)
    execute_once("dropbox")
    execute_once("seafile-applet")

@hook.subscribe.screen_change 
def restart_on_screen_change(qtile, ev): 
    setup_screens()
    update_wallpaper(WALLPAPER)
    qtile.cmd_restart() 
