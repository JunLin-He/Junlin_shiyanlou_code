#!/usr/bin/env python3
import sys
from multiprocessing import Pipe, Process

# Define the pipe - global variable
conn1_send, conn1_receive = Pipe()
conn2_send, conn2_receive = Pipe()

class Config(object):
	"""docstring for Config"""
	def __init__(self, cfg_name):
		self.cfg_name = cfg_name

	def get_social_insurance(self):
		insurance = {}
		with open(self.cfg_name) as file:
			for line in file:
				# Handle the configuration data
				list = line.split("=")
				list[0] = list[0].strip()		# Name of insurance item
				list[1] = list[1].strip()		# Value of insurance item
				insurance[list[0]] = float(list[1]) #'%.2f' % list[1]		

		#return insurance
		conn1_send.send(insurance)


class UserData(object):
	"""docstring for UserData"""
	def __init__(self, userdata_name):
		self.userdata_name = userdata_name

	def get_user_data(self):
		employee_salary = {}
		with open(self.userdata_name) as file:
			for line in file:
				# Handle the employee salary data
				list = line.split(",")
				employee_salary[list[0]] = int(list[1])	 # Translate the string type into integer 
		
		return employee_salary

	def calculate_salary(self, employee_salary):
		insurance = conn1_receive.recv()
		calculated_salary = []
		# Get the employee ID and corresponding salary 
		for k in employee_salary:

			# Determind the calculate number by insurance JiShuL and insurance JiShuH
			if employee_salary[k] < insurance["JiShuL"]:
				cal_num = insurance["JiShuL"]
			elif insurance["JiShuL"] < employee_salary[k] < insurance["JiShuH"]:
				cal_num = employee_salary[k]
			else:
				cal_num = insurance["JiShuH"]

			# Get the amount of insurance
			social_insurance = cal_num * (insurance["YangLao"] + insurance["YiLiao"] + insurance["ShiYe"] + 
							insurance["GongShang"] + insurance["ShengYu"] + insurance["GongJiJin"])

			# Get the tax and salary_after_tax
			MARKING_POINT = 3500
			if employee_salary[k] <= 3500:
				tax = 0
				aftertax_salary = employee_salary[k] - social_insurance
				
			else:
				social_insurance = employee_salary[k] * 0.165
				taxable_income = employee_salary[k] - social_insurance - MARKING_POINT
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
				aftertax_salary = employee_salary[k] - tax - social_insurance				

			# Output Format: ID,salary,insurance,tax,salary_after_tax
			social_insurance = '{:.2f}'.format(social_insurance)
			tax = '{:.2f}'.format(tax)
			aftertax_salary = '{:.2f}'.format(aftertax_salary)
			text = str(k) + ',' + str(employee_salary[k]) + ',' + social_insurance + ',' + tax + ',' + aftertax_salary
			calculated_salary.append(text)

		#return calculated_salary
		conn2_send.send(calculated_salary)


def check(argv):
	if len(argv) != 7:
		print("Usage: ./homework3 -c <config_filename> -d <user_filename> -o <output_filename>")
		exit()
	


def write_data(filename):
	calculated_salary = conn2_receive.recv()
	with open(filename, 'w') as file:
		for line in calculated_salary:
			file.write(line)
			file.write('\n')

def main():

	# Check the validation of the file and the data
	check(sys.argv)

	####for test
	#sys_argv1 = "configuration.cfg"
	#sys_argv2 = "employee_salary.csv"
	#sys_argv3 = "employee_salary_list.csv"
	####for test

	# Get the insurance calculate rule from the configuration.cfg
	config = Config(sys.argv[2])
	#insurance = config.get_social_insurance()	
	Process(target=config.get_social_insurance).start()

	# Get the salary from the employee_salary.csv
	userdata = UserData(sys.argv[4])
	employee_salary = userdata.get_user_data()
	#calculated_salary = userdata.calculate_salary(employee_salary, insurance)
	Process(target=userdata.calculate_salary, args=(employee_salary, )).start()

	# Write the result into the employee_salary_list.csv
	#write_data(sys.argv[6], calculated_salary)
	Process(target=write_data, args=(sys.argv[6], )).start()


if __name__ == '__main__':
	main()

