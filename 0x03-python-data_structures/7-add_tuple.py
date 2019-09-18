#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list1 = list(tuple_a)
    list2 = list(tuple_b)
    for x in range(0, 2):
        if len(list1) < 2:
            list1.append(0)
        if len(list2) < 2:
            list2.append(0)
    tuple_a = tuple(list1)
    tuple_b = tuple(list2)
    return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
