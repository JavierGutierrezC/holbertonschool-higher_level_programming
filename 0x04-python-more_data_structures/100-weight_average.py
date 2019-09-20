#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    multir = 0
    multid = 0
    for x in my_list:
        multid = multid + (x[0] * x[1])
        multir = multir + (x[1])
    return(multid / multir)
