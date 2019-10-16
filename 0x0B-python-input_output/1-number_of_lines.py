#!/usr/bin/python3
def number_of_lines(filename=""):
    linecount = 0
    with open(filename, encoding="UTF-8") as file_2:
        for a_line in file_2:
            linecount += 1
        return(linecount)
