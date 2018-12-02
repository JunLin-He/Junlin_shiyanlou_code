"myfact module"

def factorial(num):
	'''
	Return the factorial value of a given number

	:arg num: We will calculate the integer value of its factorial

	:return: Factorial value will be -1 if the argument passed is negative
	'''
	if num >= 0:
		if num == 0:
			return 1	
		return num * factorial(num - 1)
	else:
		return -1