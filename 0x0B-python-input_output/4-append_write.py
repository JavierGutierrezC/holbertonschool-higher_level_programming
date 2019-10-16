#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="UTF-8") as file_5:
        return(file_5.write(text))
