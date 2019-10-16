#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="UTF-8") as File_4:
        return(File_4.write(text))
