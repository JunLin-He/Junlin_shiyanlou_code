#!/usr/bin/env python3
import sys, getopt, configparser, datetime
from multiprocessing import Queue, Process
from datetime import datetime

# 定义进程间通信的队列
queue = Queue()

class UserData(object):
	"""UserData Class"""
	"""获取并处理user.csv的员工数据，并计算每一个员工的税后工资等"""
	def __init__(self, userdata_name):
		self.userdata_name = userdata_name

	# 读取user.csv的数据[工号:税前工资]并整合到dict对象中
	def get_user_data(self):
		employee_salary = {}
		with open(self.userdata_name) as file:
			for line in file:
				# Handle the employee salary data
				list = line.split(",")
				employee_salary[list[0]] = int(list[1])	 # Translate the string type into integer 
		return employee_salary

	# 计算税后工资，返回一个list对象，其内容如下：工号,税前工资,社保金额,个税金额,税后工资,计算时间
	def calculate_salary(self, employee_salary, insurance_tmp):	
		insurance = {}
		calculated_salary = []
		t = datetime.now()
		cal_time = datetime.strftime(t, '%Y-%m-%d %H:%M:%S')

		# 将insurance_tmp的value从string转换成float
		for k in insurance_tmp:
			try:
				insurance[k] = float(insurance_tmp[k])
			except TypeError:
				print('./homework3 -c <config_filename> -d <user_filename> -o <output_filename>')
				sys.exit(2)
			
		for k in employee_salary:

			# 计算工资对应的缴费基数
			if employee_salary[k] < insurance["jishul"]:
				cal_num = insurance["jishul"]
			elif insurance["jishul"] < employee_salary[k] < insurance["jishuh"]:
				cal_num = employee_salary[k]
			else:
				cal_num = insurance["jishuh"]

			# 获取五险一金总额
			social_insurance = cal_num * (insurance["yanglao"] + insurance["yiliao"] + insurance["shiye"] + 
							insurance["gongshang"] + insurance["shengyu"] + insurance["gongjijin"])

			# 获取应缴税和税后工资
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
			text = str(k) + ',' + str(employee_salary[k]) + ',' + social_insurance + ',' + tax + ',' + aftertax_salary + ',' + cal_time
			calculated_salary.append(text)

		# 通过queue通道将该进程计算所得的税后工资发送到write()函数中
		queue.put(calculated_salary)


"""检查参数是否合法"""
def check(argv):
	
	check_return = {}
	check_valid = []

	# 确保命令行参数除了文件名一共有6个或8个
	if len(argv) != 8 and len(argv) != 6:
		print('./homework3 -C cityname -c configfile -d userdata -o resultdata')
		sys.exit(2)

	try:
		# -c -d -o对应的参数均为必输
		opts, args = getopt.getopt(argv, "hC:c:d:o:", ["help"])
	except getopt.GetoptError:
		print('./homework3 -c <config_filename> -d <user_filename> -o <output_filename>')
		sys.exit(2)

	for opt, arg in opts:
		if opt in ('-h', '--help'):
			print('./homework3 -c <config_filename> -d <user_filename> -o <output_filename>')
			sys.exit(2)
		elif opt == '-C':
			check_return['cityname'] = arg.upper()
		elif opt == '-c':
			check_return['cfgfile'] = arg
			check_valid.append('X')
		elif opt == '-d':
			check_return['userdata'] = arg
			check_valid.append('X')
		elif opt == '-o':
			check_return['output'] = arg
			check_valid.append('X')
		elif opt not in ('-c', '-d', '-o'):	# 如果输入了非法参数，则报错
			print('./homework3 -c <config_filename> -d <user_filename> -o <output_filename>')
			sys.exit(2)

	# 限制-c -d -o都必须要有且只有一个对应的参数
	if len(check_valid) != 3:
		print('./homework3 -c <config_filename> -d <user_filename> -o <output_filename>')
		sys.exit(2)

	return check_return	# 返回值包括了：城市名、配置文件名、用户数据文件名、输出文件名


"""将结果写入输出文件中"""
def write_data(filename):
	# 通过queue通道获取计算税后工资的进程发出的计算结果
	calculated_salary = queue.get()
	with open(filename, 'w') as file:
		for line in calculated_salary:
			file.write(line)
			file.write('\n')

def main(argv):

	# 检查参数的合法性
	check_return = check(argv)

	#如果没有-C参数，则用DEFAULT去读配置文件
	try:
		cityname = check_return['cityname']
	except KeyError:
		cityname = 'DEFAULT'

	# 根据城市名获取配置文件
	config = configparser.ConfigParser()	# 创建一个config对象
	config.read(check_return['cfgfile'])	# 根据配置文件的文件名读取配置，传入参数为配置文件的名称
	
	userdata = UserData(check_return['userdata'])	# 传入参数为员工税前工资的数据文件名称
	employee_salary = userdata.get_user_data()	# 获取员工的税前工资

	# 启用进程计算员工的税后工资
	Process(target=userdata.calculate_salary, args=(employee_salary, config[cityname])).start()

	# 启用进程将结果写入输出文件中
	Process(target=write_data, args=(check_return['output'], )).start()


"""Boost the program"""
if __name__ == '__main__':
	main(sys.argv[1:])

 