#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

# Restore background from previous session
~/.fehbg &

picom --config $HOME/.config/qtile/scripts/picom.conf &
