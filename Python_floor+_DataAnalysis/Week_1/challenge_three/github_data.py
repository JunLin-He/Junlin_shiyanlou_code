""" dependency: requests, pandas
"""

import requests
import pandas as pd

def issues(repo):
	""" GitHub data collection
	"""
	url = 'https://api.github.com/repos/' + repo + '/issues'
	raw = requests.get(url)
	# Handle the data
	# Question: how to handle the exception?
	# if type(raw.json()) == list: ???
	out_data = []
	for r_json in raw.json():
		tmp_dic = {}
		tmp_dic['number'] = r_json['number']
		tmp_dic['title'] = r_json['title']
		tmp_dic['user_name'] = r_json['user']['login']
		out_data.append(tmp_dic)
	issues_df = pd.DataFrame(out_data)
	return issues_df

id = issues("numpy/numpy")	# Test case
id.to_csv("test.csv")
