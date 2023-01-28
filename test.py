#!usr/bin/python3

# test.py
# Version 1.0.0
# 1/11/23

# Written By: Mason R. Ware

# This file represents a working implented program in python, albeit a 
# barebone one. It's purpose is to test out the capabilities of the monocmd

import monocmd.argparser as argparser
from pprint import pprint


# helper function to reverse a string
def reverse(string: str) -> str:
    return string[::-1]


if __name__ == "__main__":
    parser = argparser.ArgumentParser("test custom arg parser")

    parser.add_argument("test")
    parser.add_argument("also")

    args = parser.parse_args()

    if args.test:
	    print("test found")
     
    pprint(vars(args))
