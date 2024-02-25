#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for elem in range(len(my_list)):
        print("{}\n".format(my_list[-(elem + 1)]))
