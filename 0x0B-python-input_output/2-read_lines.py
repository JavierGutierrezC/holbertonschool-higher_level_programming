#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="UTF-8") as file_3:
        if nb_lines <= 0:
            print(file_3.read(), end="")
        else:
            for x in range(nb_lines):
                print(file_3.readline(), end="")
