#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        print(None)
    elif idx >= len(my_list):
        print(None)
    else:
        for x in range(len(my_list)):
            if x == idx:
                return(my_list[x])
