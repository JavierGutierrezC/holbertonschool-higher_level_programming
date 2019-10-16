#!/usr/bin/python3
def read_file(filename=""):
    """comment"""
    with open(filename, encoding="UTF-8") as files_1:
        print(files_1.read(), end="")
