#!usr/bin/python3

# argparser.py
# Version 1.0.0
# 1/14/23

# Written By: Mason R. Ware

class Argument:
    def __init__(self, kwarg: str, help: str):
        return

class ParsedCMD:
    def __init__(self, *args):
        for idx, item in enumerate(args):
            setattr(self, f"{idx}", item)

class ArgumentParser:
    description: str = ''
    
    def __init__(self, description=''):
        self.description = description
    
    def add_argument(kwarg: str, help: str, param: bool = False):
        return
    
    def parse_args():
        return
        # TODO hang on user input?