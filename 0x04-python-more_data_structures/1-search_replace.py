#!/usr/bin/python3
def search_replace(my_list, search, replace):
    re_list = []
    for elem in range(len(my_list)):
        if my_list[elem]== search:
            re_list.append(replace)
        else:
            re_list.append(my_list[elem])
    return re_list