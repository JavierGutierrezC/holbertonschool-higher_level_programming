#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        print(my_list)
    elif idx > len(my_list):
        print(my_list)
    else:
        for x in range(len(my_list)):
            if x == idx:
                my_list[x] = element
                return(my_list)
        return(my_list)