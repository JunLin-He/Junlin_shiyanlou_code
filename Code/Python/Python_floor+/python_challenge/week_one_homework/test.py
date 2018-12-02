import sys

salary = sys.argv
temp_list = []
for i in range(1, len(salary)):
	temp_list.append(salary[i].split())

tmp_dic = dict(temp_list)
print tmp_dic