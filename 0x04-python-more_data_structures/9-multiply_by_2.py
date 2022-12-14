#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dic = {}
    for i in a_dictionary:
        a = a_dictionary[i] + a_dictionary[i]
        my_dic[i] = a
    return my_dic