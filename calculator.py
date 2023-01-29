#!usr/bin/python3

# test.py
# Version 1.0.0
# 1/11/23

# Written By: Mason R. Ware

# This file represents a working implented program in python, albeit a 
# barebone one. It's purpose is to test out the capabilities of the monocmd

from pprint import pprint

class Calculator:
    def add(x: int, y: int):
        return x+y
    
    def subtract(x: int, y: int):
        return x-y
    
    def multiply(x: int, y: int):
        return x*y
    
    def divide(x:int, y:int):
        return x/y
    
def function():
    print("functional call")

if __name__ == "__main__":
    ###
    import monocmd.argparser as argparser

    parser = argparser.ArgumentParser("test custom arg parser")
    
    parser.add_argument("test")
    
    args = parser.parse_args()
    
    if args.test:
        print("heyo")
    ###
