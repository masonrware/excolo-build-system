#!usr/bin/python3

# monocmd.py
# Version 1.0.0
# 1/24/23

# Written By: Mason R. Ware

import monocmd.argparser


class Configuration:
    def __init__(self) -> None:
        pass


class YAMLParser:
    def __init__(self, sourcefile: str = "") -> None:
        self.sourcefile = sourcefile


class Monocmd:
    def __init__(self) -> None:
        pass

    def _make_alias(self):
        # run bash code to make an alias for the main file
        pass

    def _parse_yaml_file(self):
        pass
    
    def _edit_python_file(self):
        pass
    
    def main(self):
        pass

if __name__ == "__main__":
    parser = argparser.ArgumentParser("test custom arg parser")

    parser.add_argument("test")

    args = parser.parse_args()

    if args.test:
        print("test found")

# TODO

# run the alias command?
# parse yaml file
# edit main python file(s) to add single line of parser declaration
#   pass in parsed yaml file object to argparser.parse_args() so that the parser can create the logic to execute if true

# TODO other

# 1. write the uninstall functionality
#   a. run the kill script from there
# 2. BUILD SYSTEM PROBLEM:
#   a. put everything in a make file with targets
#       i. have a ./config file as well

# ! python command to run an individual method

# python3 -c 'from calculator import reverse; print(reverse("hello"))'
