#!/bin/bash

# TODO incorperate environmental variables?
# add an alias for running a program

#! TODO alias command fuck me?

grep -qxF 'alias mason="python3.8 ~/Desktop/bashRC/test.py"' ~/.bashrc \
|| echo 'alias mason="python3.8 ~/Desktop/bashRC/test.py"' >> ~/.bashrc

grep -qxF 'alias mason="python3.8 ~/Desktop/bashRC/test.py"' ~/.config/fish/config.fish \
|| echo 'alias mason="python3.8 ~/Desktop/bashRC/test.py"' >> ~/.config/fish/config.fish

source ~/.bashrc
source ~/.config/fish/config.fish