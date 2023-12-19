#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
	my_list = []
	for i in range(list_length):
		try:
			my_list.append(my_list_1[i]/my_list_2[i])
		except TypeError as err:
			print("wrong type")
			my_list.append(0)
		except ZeroDivisionError as err:
			print("division by 0")
			my_list.append(0)
		except IndexError as err:
			print("out of range")
			my_list.append(0)
		finally:
			pass
		return my_list