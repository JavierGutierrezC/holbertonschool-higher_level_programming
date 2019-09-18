#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copylis = my_list.copy[0:]
    if idx < 0:
        return(my_list)
    elif idx >= len(my_list):
        return(my_list)
    else:
        copylis[idx] = element
        return(my_list)
