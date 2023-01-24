#!usr/bin/python3

# monocmd.py
# Version 1.0.0
# 1/24/23

# Written By: Mason R. Ware

# TODO

# 1. run start script
# 2. parse yaml file
# 3. edit main python file(s)
#   a. maybe just use argparse instead with flags (who cares)
#       i. maybe give the option...
# 4. move onto other

# TODO other

# 1. write the uninstall functionality
#   a. run the kill script from there
# 2. BUILD SYSTEM PROBLEM:
#   a. this is a tricky one because ideally, the user
#      installs the command from homebrew, etc... and 
#      then the command will automatically be added as
#      an alias using smth like this (?):
#
#~/bin
##!/bin/bash
#BASE="https://api.blah.com"
#
#sudo bash -c "curl -s $BASE/mycmd > /usr/bin/mycmd"
#sudo chmod uga+x /usr/bin/mycmd
#
#   b.! look into maybe just using a makefile or a
#      configure file with a makefile?


