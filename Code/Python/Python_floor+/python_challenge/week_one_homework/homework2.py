#!/usr/bin/env python3
import sys

def check_input(list):
	for inx, val in enumerate(list):
		if inx != 0:
			tmp_list = val.split(':')

			try:
				salary = int(tmp_list[1])		
			except SyntaxError:
				print("salary must be integer!")
				exit(-1)
			except ValueError:
				print("salary must be integer!")
				exit(-1)

			if salary < 0:
				print("Salary: {0} is irrational!".format(salary))
				exit(-1)	

def calculate_tax(salary):
	salary = int(salary)
	MARKING_POINT = 3500
	social_insurance = salary * 0.165
	if salary <= 3500:
		aftertax_salary = salary - social_insurance
		aftertax_salary = '{:.2f}'.format(aftertax_salary)
		return aftertax_salary
	else:
		social_insurance = salary * 0.165
		taxable_income = salary - social_insurance - MARKING_POINT
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
		aftertax_salary = salary - tax - social_insurance
		aftertax_salary = '{:.2f}'.format(aftertax_salary)
		return aftertax_salary


def main():

	# Determine if the input parameter is legal
	argv_length = len(sys.argv)
	if argv_length < 2:
		print("usage: ./homework1 [person_number1:salary1] ... [person_numbern:salaryn]")
		return

	# Check the invalid input
	check_input(sys.argv)

	new_employee = []

	# index：当前遍历的次数
	# employee：遍历出来的对象
	for index, employee in enumerate(sys.argv):
		if index == 0:
			continue	# 当前对象为文件名本身
		else:
			tmp_employee = employee.split(':')	# 获取字符串分割得到的数组-》 103:3500
			aftertax_salary = calculate_tax(tmp_employee[1])	# 计算该员工的税后工资，返回值为float型			
			new_employee.append(tmp_employee[0] + ':' + str(aftertax_salary))	# 拼接成103:3500的形式，并增加到list中

	for val in new_employee:
		print(val)	# 依次打印工号：工资

if __name__ == '__main__':
	main()


