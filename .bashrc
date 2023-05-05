### ENVIRONMENTAL VARIABLES ###

export TERM="xterm-256color"
export TERMINAL='alacritty'
export EDITOR='nano'
export VISUAL='nano'
export HISTCONTROL=ignoredups:erasedups
export HISTORY_IGNORE="(ls|cd|pwd|exit|sudo reboot|history|cd -|cd ..)"

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

### BASH SETTINGS ###

# Ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

HISTSIZE=10000
HISTFILESIZE=10000

shopt -s autocd # change to named directory
shopt -s cdspell # autocorrects cd misspellings
shopt -s cmdhist # save multi-line commands in history as single line
shopt -s dotglob
shopt -s histappend # do not overwrite history
shopt -s expand_aliases # expand aliases
shopt -s checkwinsize # checks term size when bash regains control

### FUNCTIONS ###

# Extract different kinds of archives. Usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   tar xf $1    ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

### ALIASES ###

# Confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

# Replace ls with exa if available
if ! command -v exa &> /dev/null
then
	alias ls='ls -1 --color=auto --group-directories-first'
	alias ll='ls -lh'
	alias la='ls -lAh'
else
	alias ls='exa -1 --color=always --group-directories-first'
	alias ll='exa -lh --color=always --group-directories-first'
	alias la='exa -lah --color=always --group-directories-first'
	alias tree='exa -T --level=1 --group-directories-first'
	alias tree2='exa -T --level=2'
	alias tree3='exa -T --level=3'
fi

alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

alias df='df -h'

alias free="free -mt"

alias pacman='sudo pacman --color auto'
alias update='sudo pacman -Syyu'

alias hw="hwinfo --short"

# Dotfiles

alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'

### PROMPT ###

eval "$(starship init bash)"

