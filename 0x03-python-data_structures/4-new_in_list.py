#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copylis = len(my_list)
    if idx < 0:
        return(my_list)
    elif idx >= copylis:
        return(my_list)
    else:
        my_list[idx] = element
        return(my_list)
