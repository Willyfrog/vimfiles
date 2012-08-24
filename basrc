#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
export GIT_PS1_SHOWDIRTYSTATE=1
PS1='[\u@\h \W]$(__git_ps1 "(%s)")\$ '

source ~/bin/virtualenv-auto-activate.sh
#cargamos git-prompt y llamamos a su funcion
source /usr/share/git/git-prompt.sh
