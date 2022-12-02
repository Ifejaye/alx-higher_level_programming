'''#!/usr/bin/python3'''
import random
number = random.randint(-10000, 10000)
if number >0:
	last_no = number % 10
else:
	last_no = -(number % 10)
if last_no > 5:
	print('Last digit of', number, 'is', last_no, 'and is greater than 5')
elif last_no == 0:
	print('Last digit of', number, 'is', last_no, 'and is 0')
elif last_no < 6:
	print('Last digit of', number, 'is', last_no, 'and is less than 6 and not 0')