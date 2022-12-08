#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for elem in a_dictionary:
            if elem == key:
                a_dictionary[elem] = value
    return a_dictionary