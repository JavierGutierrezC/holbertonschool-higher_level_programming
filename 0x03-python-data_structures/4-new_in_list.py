#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copylis = my_list.copy()
    if idx < 0:
        return(my_list)
    elif idx > len(my_list):
        return(my_list)
    else:
        for x in range(len(copylis)):
            if x == idx:
                copylis[x] = element
                return(copylis)
        return(my_list)
