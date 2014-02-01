#!/bin/sh

#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)
#

#exec openbox-session

#setxkbmap -layout us -variant altgr-intl -option nodeadkeys
#setxkbmap -option "ctrl:nocaps"
#xrdb -merge .Xresources
##xrandr --output LVDS1 --left-of VGA1
##xcompmgr &
#( ( sleep 10 && /usr/bin/xscreensaver -no-splash -display :0.0 ) & )
#sh .fehbg &
##exec /usr/bin/awesome
exec /usr/bin/qtile
