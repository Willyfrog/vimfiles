# -*- coding: utf-8 -*-
# Note that since qtile configs are just python scripts, you can check for
# syntax and runtime errors by just running this file as is from the command
# line, e.g.:
#
#    python config.py

from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from subprocess import Popen, check_output, PIPE, STDOUT
from time import sleep
from os import path
import re


# Theme
#
class Theme(object):
    bar = dict(
         opacity=0.9,
         background='1a1a1a'
         )

    class Layout(object):
        border_args = dict(
            border_normal='#000000',
            border_focus='#000000',
            border_width=2,
        )

    class Widget(object):
        icons_path = '/user/share/icons/Faenza-Dark/status/24'
        default = dict(
                padding=1,
                fontsize=14,
                font='Tamsyn',
                foreground='a0a0a0'
                )
        group_box = dict(default.items() + dict(
                other_screen_border='880000',
                padding=3,
                urgent_alert_method='text',
                fontsize=12,
                ).items())
        window_name = dict(default.items() + dict(
                ).items())
        # backlight = dict(default.items() + dict(
        #         backlight_name='intel_backlight'
        #         ).items())
        volume = dict(default.items() + dict(
                theme_path=icons_path
                ).items())
        battery_icon = dict(default.items() + dict(
                theme_path=icons_path,
                battery_name='BAT1'
                ).items())
        battery = dict(default.items() + dict(
                padding=0,
                battery_name='BAT1',
                charge_char='',
                discharge_char='',
                energy_now_file='charge_now',
                energy_full_file='charge_full',
                power_now_file='current_now',
                update_delay=4
                ).items())
        #yahoo_weather = dict(default.items() + dict(
        #        location='Madrid, SP'
        #        ).items())
        clock = dict(default.items() + dict(
                fmt='%d.%m.%Y // %H:%M',  #'%a, %d de %b, %H:%M',
                fontsize=14,
                padding=10
                ).items())
        current_layout = dict(default.items() + dict(
                fontsize=12,
                foreground='7070ff'
                ).items())


# Screens
#
screens = [
    Screen(
        top = bar.Bar([
            widget.GroupBox(**Theme.Widget.group_box),
            widget.Sep(padding=10),
            widget.CurrentLayout(**Theme.Widget.current_layout),
            widget.Sep(padding=10),
            widget.WindowName(**Theme.Widget.window_name),
            widget.Prompt(**Theme.Widget.default),
            #widget.Backlight(**Theme.Widget.backlight),
            widget.Volume(**Theme.Widget.volume),
            widget.BatteryIcon(**Theme.Widget.battery_icon),
            widget.Battery(**Theme.Widget.battery),
            widget.Systray(),
            widget.Clock(**Theme.Widget.clock),
            #widget.YahooWeather(**Theme.Widget.yahoo_weather),
            #widget.Notify(foreground='#ffff00')
        ], 22, **Theme.bar)
    ),
    Screen(
        top = bar.Bar([
            widget.GroupBox(**Theme.Widget.group_box),
            widget.Sep(padding=10),
            widget.CurrentLayout(**Theme.Widget.current_layout),
            widget.Sep(padding=10),
            widget.WindowName(**Theme.Widget.window_name),
        ], 22, **Theme.bar)
    ),
]


# Key bindings
#
mod = "mod4"
alt = "mod1"
shift = "shift"
ctrl = "control"
keys = [
    Key([shift, alt], "q",       lazy.shutdown()),

    #Key([mod, ctrl], "j",        lazy.layout.section_down()),  # for tree layout
    #Key([mod, ctrl], "k",        lazy.layout.section_up()),  # for tree layout
    #Key([mod, ctrl], "h",        lazy.layout.collapse_branch()),  # for tree layout
    #Key([mod, ctrl], "l",        lazy.layout.expand_branch()),  # for tree layout

    Key([mod, ctrl], "k",
        lazy.layout.grow(),              # xmonad-tall
        lazy.layout.decrease_nmaster()), # Tile
    Key([mod, ctrl], "j",
        lazy.layout.shrink(),            # xmonad-tall
        lazy.layout.increase_nmaster()), # Tile
    Key([mod, ctrl], "l",
        lazy.layout.delete(),            # Stack
        lazy.layout.increase_ratio(),    # Tile
        lazy.layout.grow()),             # xmonad-tall
    Key([mod, ctrl], "h",
        lazy.layout.add(),               # Stack
        lazy.layout.decrease_ratio(),    # Tile
        lazy.layout.shrink()),           # xmonad-tall

    Key([mod], "k",              lazy.layout.down()),
    Key([mod], "j",              lazy.layout.up()),
    Key([mod], "h",              lazy.layout.previous()),
    Key([mod], "l",              lazy.layout.next()),

    Key([mod, alt], "h",         lazy.to_screen(0)),
    Key([mod, alt], "l",         lazy.to_screen(1)),

    Key([ctrl, alt], "Up",       lazy.to_screen(0), lazy.screen.prevgroup()),
    Key([ctrl, alt], "Down",     lazy.to_screen(0), lazy.screen.nextgroup()),
    Key([ctrl, alt, shift], "Up", lazy.to_screen(1), lazy.screen.prevgroup(), lazy.to_screen(0)),
    Key([ctrl, alt, shift], "Down", lazy.to_screen(1), lazy.screen.nextgroup(), lazy.to_screen(0)),

    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up()),       # Stack, xmonad-tall
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down()),     # Stack, xmonad-tall

    Key([mod, shift], "space",
        lazy.layout.rotate(),
        lazy.layout.flip()),             # xmonad-tall

    Key([alt, shift], "Tab",     lazy.layout.previous()),
    Key([alt], "Tab",            lazy.layout.next()),

    Key([mod, shift], "Return",  lazy.layout.toggle_split()),
    Key([mod, shift], "f",       lazy.window.toggle_floating()),

    Key([alt], "space",          lazy.nextlayout()),
    Key([alt, shift], "space",   lazy.prevlayout()),

    Key([mod], "x",              lazy.window.kill()),
    Key([mod, ctrl], "r",        lazy.restart()),

    # interact with prompts
    Key([mod], "r",              lazy.spawncmd()),
    Key([mod], "g",              lazy.switchgroup()),

    # start specific apps
    Key([alt], "F2",
            lazy.spawn("dmenu_run -p run -fn 'Terminus-13' -nb '#202020' -nf '#ffffff'")),
    Key([mod], "Return",         lazy.spawn("urxvt")),
    Key([mod, alt], "Return",    lazy.group["code"].toscreen()),
    Key([mod], "b",              
            lazy.spawn("chromium-browser"),
            lazy.group["www"].toscreen()),
    Key([mod, alt], 'b',         lazy.group["www"].toscreen()),

    # Multimedia keys
    Key([], "XF86AudioRaiseVolume",  lazy.spawn("amixer -c 0 -q set Master 2dB+")),
    Key([], "XF86AudioLowerVolume",  lazy.spawn("amixer -c 0 -q set Master 2dB-")),
    Key([], "XF86AudioMute",         lazy.spawn("amixer -D pulse -q set Master toggle")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
    Key([], "XF86MonBrightnessUp",   lazy.spawn("xbacklight -inc 10")),
    #Key([], "XF86TouchpadToggle",   lazy.spawn("synclient TouchpadOff=$(synclient -l | grep -c 'TouchpadOff.*=.*0')")),
    Key([], 'XF86Calculator',        lazy.spawn('xcalc')),
    Key([], 'XF86Mail',              lazy.spawn('chromium-browser "http://mail.google.com"'), lazy.group["www"].toscreen()),
    Key([], 'XF86HomePage',          lazy.to_screen(0), lazy.group["code"].toscreen()),

    # lock screen
    Key([ctrl, alt], "l", lazy.spawn("screenlock")),
]


# Mouse
#
mouse = [
    Drag([mod], "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2",
        lazy.window.bring_to_front())
]


# Groups
#
groups = []
# groups.extend([
#     Group('www', layout='max',
#         matches=[Match(wm_class=["chromium", "Chromium", "Navigator", "Iceweasel"])]),
#     Group('code', layout='max'),
# ])
for i in ["1", "2", "3", "4", "5"]:
    groups.append(Group(i, layout='max'))
# groups.extend([
#     #Group('gvim', layout='max', persist=False, init=False, screen_affinity=1, matches=[Match(wm_class=["gvim", "Gvim"])]),
#     Group('music', layout='max', persist=False, init=False),
#     Group('gimp', layout='gimp', persist=False, init=False,
#         matches=[Match(wm_class=['gimp', 'Gimp'])]),
#     Group('screen2', layout='max'),
# ])
for i, group in enumerate(groups):
    keys.extend([
        Key([mod], str(i + 1), lazy.group[group.name].toscreen()),
        Key([mod, shift], str(i + 1), lazy.window.togroup(group.name))
    ])


# Layouts
#
layouts = [
    layout.Max(),
    #layout.TreeTab(sections=['Surfing', 'E-mail', 'Docs', 'Incognito']),
    layout.Stack(stacks=2, **Theme.Layout.border_args),
    layout.MonadTall(),
    layout.Tile(),
    #layout.Zoomy(),

    # a layout just for gimp
    layout.Slice('left', 192, name='gimp', role='gimp-toolbox',
         fallback=layout.Slice('right', 256, role='gimp-dock',
         fallback=layout.Stack(stacks=1, **Theme.Layout.border_args))),
]


# Hooks
#
def is_running(process):
    s = Popen(["ps", "axuw"], stdout=PIPE)
    for x in s.stdout:
        if re.search(process, x):
            return True
    return False


def execute_once(process):
    if not is_running(process):
        return Popen(process.split())


def cmd_get(process):
    return check_output("%s; exit 0;" % process, stderr=STDOUT, shell=True)


@hook.subscribe.client_new
def dialogs(window):
    if (window.window.get_wm_type() == 'dialog'
            or window.window.get_wm_transient_for()
            ):
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


def setup_screens():
    num_screens = int(cmd_get("xrandr|grep -c \ connected"))
    if num_screens == 1:
        execute_once("xrandr " +
        "--output HDMI1 --off " +
        "--output LVDS1 --mode 1366x768 --pos 0x0 --rotate normal " +
        "--output DP1 --off " +
        "--output VGA1 --off")
    else:
        execute_once("xbacklight -set 100")
        if bool(int(cmd_get("xrandr|grep -c \"VGA[0-9]* connected\""))):
            execute_once("xrandr --output HDMI1 --off " + 
                         "--output LVDS1 --mode 1366x768 --pos 0x232 --rotate normal " +
                         "--output DP1 --off " +
                         "--output VGA1 --primary --mode 1920x1080")

            # execute_once("xrandr " +
            # "--output HDMI1 --off " +
            # "--output DP1 --off " +
            # "--output VGA1 --primary --mode 1920x1080 --rotate normal --right-of " +
            # "--output LVDS1 --mode 1366x768 --pos 0x0 --rotate normal --pos 277x1080")
        elif bool(int(cmd_get("xrandr|grep -c \"HDMI[0-9]* connected\""))):
            execute_once("xrandr --output VGA1 --off " + 
                         "--output LVDS1 --mode 1366x768 --pos 0x232 --rotate normal " +
                         "--output DP1 --off " +
                         "--output HDMI1 --primary --mode 1920x1080")
            # execute_once("xrandr " +
            # "--output VGA1 --off " +
            # "--output DP1 --off " +
            # "--output HDMI1 --primary --mode 1920x1080 --rotate normal --right-of " +
            # "--output LVDS1 --mode 1366x768 --pos 0x0 --rotate normal --pos 1920x312")
        else:
            execute_once("xrandr " +
            "--output HDMI1 --off " +
            "--output LVDS1 --mode 1366x768 --pos 0x0 --rotate normal " +
            "--output DP1 --off " +
            "--output VGA1 --off")


@hook.subscribe.startup
def startup():
    execute_once("xbacklight -set 30")
    #execute_once("xcompmgr")
    execute_once("sh ~/.fehbg")
    #execute_once("nm-applet")
    #execute_once("xcaliber --bR=256 --bG=256 --bB=200 --gR=1.0 --gG=1.0 --gB=0.85")
    #execute_once("sudan")
    #execute_once("xautolock -time 1 -locker screenlock")
    execute_once("xscreensaver -no-logo")
    #execute_once("nice -n 19 dropbox start")
    #execute_once("nice -n 19 xrdb -merge ~/.Xresources")
    #execute_once("irssi_notifier")
    setup_screens()


@hook.subscribe.screen_change 
def restart_on_screen_change(qtile, ev): 
    setup_screens()
    qtile.cmd_restart() 
