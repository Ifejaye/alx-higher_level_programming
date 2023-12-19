#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end=' ')
            i = i + 1
        except (ValueError, IndexError):
            i = i + 1
        finally:
            pass
    print()  # Print a new line after the integers
    return i
