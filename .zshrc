### Navigation Options ###

setopt autocd                                                   # If only directory path is entered, cd there.

### History options ###

setopt appendhistory                                            # Immediately append history instead of overwriting
setopt inc_append_history                                       # Save commands are added to the history immediately, otherwise only when shell exits.
setopt histignoredups                                           # Don't save a command if it's the same as the previous one
setopt histignorespace                                          # Don't save commands that start with space
HISTFILE=~/.zhistory
HISTSIZE=10000
SAVEHIST=10000

### Auto-completion options ###

setopt extendedglob                                             # Extended globbing. Allows using regular expressions with *
setopt nocaseglob                                               # Case insensitive globbing
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}'
zstyle ':completion:*' rehash true                              # automatically find new executables in path 

autoload -U compinit && compinit

### Miscellaneous options ###

setopt nobeep                                                   # No beep

### Plugins ###

source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh

### Aliases ###

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

alias note='nano --operatingdir=$HOME/Documents'

### Prompt ###

eval "$(starship init zsh)"
