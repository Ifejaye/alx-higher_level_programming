def print_reversed_list_integer(my_list=[]):
    for elem in range(len(my_list)):
        print("{}".format(my_list[-(elem + 1)]))


my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
