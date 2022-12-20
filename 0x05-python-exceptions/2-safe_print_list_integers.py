def safe_print_list_integers(my_list=[], x=0):
	for elem in range(my_list):
		while (elem < x):
			try:
				print ("{:d}".format(my_list[elem]))
			except:
				pass
