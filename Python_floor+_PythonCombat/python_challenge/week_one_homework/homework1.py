#!/usr/bin/env python3
import sys

def main():
	SOCIAL_INSURANCE = 0
	MARKING_POINT = 3500

	# Determine if the input parameter is legal
	argv_length = len(sys.argv)
	if argv_length != 2:
		print("usage: ./homework1 salary")
		return

	try:
		salary = int(sys.argv[1])
	except SyntaxError:
		print("salary must be integer!")
		return
	except ValueError:
		print("salary must be integer!")
		return	
	
	if salary <= 3500:
		tax = 0
	else:
		taxable_income = salary - SOCIAL_INSURANCE - MARKING_POINT
		if taxable_income <= 1500:
			tax_rate = 0.03
			quick_deduction = 0
		elif 1500 < taxable_income <= 4500:
			tax_rate = 0.10
			quick_deduction = 105
		elif 4500 < taxable_income <= 9000:
			tax_rate = 0.20
			quick_deduction = 555
		elif 9000 < taxable_income <= 35000:
			tax_rate = 0.25
			quick_deduction = 1005
		elif 35000 < taxable_income <= 55000:
			tax_rate = 0.30
			quick_deduction = 2755
		elif 55000 < taxable_income <= 80000:
			tax_rate = 0.35
			quick_deduction = 5505
		else:
			tax_rate = 0.45
			quick_deduction = 13505

		tax = taxable_income * tax_rate - quick_deduction
		
	print('{0:.2f}'.format(tax))

if __name__ == '__main__':
	main()