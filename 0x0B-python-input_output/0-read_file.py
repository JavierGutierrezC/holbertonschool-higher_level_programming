#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding="UTF-8") as file_1:
        print(file_1.read(), end="")
