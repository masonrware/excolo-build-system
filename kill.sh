#!/bin/bash

# TODO incorperate environmental variables?
# remove aliases from bashrc and from fish config

grep -vwF 'alias mason="python3.8 ~/Desktop/bashRC/test.py"' ~/.bashrc > ~/.bashrc

grep -vwF 'alias mason="python3.8 ~/Desktop/bashRC/test.py"' ~/.config/fish/config.fish > ~/.config/fish/config.fish

source ~/.bashrc
source ~/.config/fish/config.fish

echo 'mason command removed from system, restarting shell...'
exec bash -l