import json

def analysis(file, user_id):
	times = 0
	minutes = 0

	with open(file) as f:
		user_datas = json.loads(f.read())
		for user_data in user_datas:
			if user_data['user_id'] == user_id:
				times += 1
				minutes += user_data['minutes']

	return times, minutes