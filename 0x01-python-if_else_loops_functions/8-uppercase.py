#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        y = ord(str[x])
        if (y >= 97 and y <= 122):
            y = y - 32
        print("{:c}".format(y), end="")
    print("")
