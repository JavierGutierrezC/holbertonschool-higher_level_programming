#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding="UTF-8") as files_2:
        print(files_2.read(), end="")
