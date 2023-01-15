#!usr/bin/python3

# test.py
# Version 1.0.0
# 1/11/23

# Written By: Mason R. Ware

import argparse

# helper function to reverse a string
def reverse(string: str) -> str:
    return string[::-1]


if __name__ == "__main__":
    # TODO build own argparse that can recognize different positional arguments?
    # otherwise just give up and use argparse with flags ew
    
    print('beta test')
    
    ## for flags:
    parser = argparse.ArgumentParser(description="beta argument testing")

    parser.add_argument("print", nargs="*", help="print out mason")

    args = parser.parse_args()

    if args.print:
        print("mason")