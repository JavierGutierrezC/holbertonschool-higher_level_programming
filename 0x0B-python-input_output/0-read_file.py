#!/usr/bin/python3
def read_file(filename=""):
    """comments"""
    with open(filename, encoding="UTF-8") as fl:
        print(fl.read(), end="")
