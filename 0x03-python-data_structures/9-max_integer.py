#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        my_list.sort()
        x = len(my_list) - 1
        return(my_list[x])
    else:
        return(None)
