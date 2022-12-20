#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	i = 0
	for elem in mylist:
		try:
			print("{}". format(mylist[elem])
			i = i + 1
		except IndexError:
			pass
		return i
