#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for elem in range(x):
        try:
            print("{:d}".format(my_list[elem]))
            i= i + 1
        except IndexError:
            pass
    return i
