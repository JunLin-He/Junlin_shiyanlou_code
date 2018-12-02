import sys, getopt

def check():
	# 确保命令行参数除了文件名一共有6个
	check_return = {}
	if len(sys.argv) != 9 and len(sys.argv) != 7:
		print('./homework3 -C cityname -c configfile -d userdata -o resultdata')
		sys.exit(2)
	try:
		# -C -c -d -o必须带参数
		opts, args = getopt.getopt(sys.argv[1:], "hC:c:d:o:", ["help"])
	except getopt.GetoptError:
		print('./homework3 -c <config_filename> -d <user_filename> -o <output_filename>')
		sys.exit(2)
	for opt, arg in opts:
		print('org:', opt)
		print('arg:', arg)
		if opt in ('-h', '--help'):
			print('./homework3 -c <config_filename> -d <user_filename> -o <output_filename>')
			sys.exit(2)
		elif opt == '-C':
			check_return['cityname'] = arg.upper()
		elif opt == '-c':
			check_return['cfgfile'] = arg
	return check_return

	#return a

def main():
	check_return = check()
	try:
		print(check_return['cityname'])
	except KeyError:
		cfg_section = 'DEFAULT'
		print(cfg_section)
	

# if the city not in the configuration file, how to report the error???


if __name__ == '__main__':
	main()


'''
salary = sys.argv
temp_list = []
for i in range(1, len(salary)):
	temp_list.append(salary[i].split())

tmp_dic = dict(temp_list)
print tmp_dic
'''


'''
import sys, getopt

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		# hi:o: 表示-h非必输 -i和-o的参数都是必输的； ifile= ofile= 表示 --ifile --ofile是必输
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print('te.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('te.py -i <inputfile> -o <outputfile>')
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	print('输入的文件为：', inputfile)
	print('输出的文件为：', outputfile)

if __name__ == "__main__":
	main(sys.argv[1:])
'''

'''
print(type(sys.argv))
print(sys.argv)
print(len(sys.argv))
'''


'''
import sys
print(type(sys.argv))
print(sys.argv)
'''

'''
for index, x in enumerate(sys.argv):
	tmp_list = x.split(':')
	if index == 0:
		continue
	else:	
		print(tmp_list[1])
'''

'''
for x in sys.argv:
	print("type: ", type(x), " value: ", x)
'''
