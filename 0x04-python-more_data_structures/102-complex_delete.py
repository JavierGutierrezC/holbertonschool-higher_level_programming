#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    newlist = list(a_dictionary.keys())
    for x in newlist:
        if value == a_dictionary.get(x):
            del a_dictionary[x]
    return (a_dictionary)
