#!/usr/bin/python3
def uniq_add(my_list=[]):
    mi_list = set(my_list)
    output = 0
    for i in mi_list:
        output += i
    return output
