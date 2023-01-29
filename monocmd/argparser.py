#!usr/bin/python3

# argparser.py
# Version 1.0.0
# 1/14/23

# Written By: Mason R. Ware

# This is an argument parser to serve as a substitute for pythons argparse.
# It is also heavily influenced in architecture and naming convention by the
# aforementioned library. It works to expect user-configured arguments and, 
# based on the user's actual cli args, returns an object with boolean 
# attributes corresponding to each user-configured arg.

from ast import List
from typing import Set

import sys

from monocmd.monocmd import Configuration

class Argument:
    name: str = ""
    help: str = ""
    param: bool = False
    description: str = ""

    def __init__(
        self, kwarg: str, help: str = "", param: bool = False, description: str = ""
    ):
        self.name = kwarg
        self.help = help
        self.param = param
        self.description = description

    def __eq__(self, other):
        return self.name == other.name

    def __nq__(self, other):
        return self.name != other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f"Argument: {self.name}"


class Namespace:
    def __init__(self, args):
        for item in args:
            setattr(self, f"{item.name}", item.param)


class ArgumentParser:
    description: str = ""
    targetFile: str = ""
    known_args: Set = set()

    def __init__(self, description: str = "", target: str = ""):
        self.description = description
        self.targetFile = target

    def add_argument(
        self, kwarg: str, help: str = "", param: bool = False, description: str = ""
    ):
        self.known_args.add(
            Argument(kwarg=kwarg, help=help, param=param, description=description)
        )

    # check runtime arguments (user_args) against known args (known_args) and create Namespace
    def _create_namespace(self, user_args: List):
        true_args: Set = set()
        namespace_args: List = list()

        # replace each user_arg string with an argument object for comparison to known arguments
        for idx, user_arg in enumerate(user_args):
            user_args[idx] = Argument(user_arg)

        user_args = set(user_args)

        # implemented Set.Union method because union wasn't working
        for known_arg in self.known_args:
            for user_arg in user_args:
                # use built in __eq__
                if user_arg == known_arg:
                    true_args.add(known_arg)

        # check if there are any unknown/invalid arguments
        invalid_args = set()
        for user_arg in user_args:
            if user_arg not in true_args:
                invalid_args.add(user_arg)

        # throw exception
        if len(invalid_args) > 0:
            raise Exception(
                f"The following arguments are unknown/invalid: {', '.join(str(v) for v in invalid_args)}"
            )

        # add all true arguments
        for true_arg in true_args:
            true_arg.param = True
            namespace_args.append(true_arg)

        # add all false arguments
        for known_arg in self.known_args:
            if known_arg not in namespace_args:
                # kind of reduntant
                known_arg.param = False
                namespace_args.append(known_arg)

        # return created namespace object
        return Namespace(namespace_args)

    def parse_args(self, config: Configuration = None):
        if config:
            ns = self._create_namespace(sys.argv[1:])
            for attr in ns.__dict__:
                if ns.__getattribute__(attr):
                    #TODO once the parsed yaml file is passed in with parse_args, we will be able to 
                    #grab its attribute based on the same name which will have the cmd as its value
                    print(attr, ns.__getattribute__(attr))
        else:
            return self._create_namespace(sys.argv[1:])
