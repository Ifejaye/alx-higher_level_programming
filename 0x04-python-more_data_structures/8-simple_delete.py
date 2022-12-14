#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    check = False
    for i in a_dictionary:
        if i == key:
            check = True

    if check == True:
        del a_dictionary[key]