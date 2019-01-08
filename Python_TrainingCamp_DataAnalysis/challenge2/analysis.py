import json
import pandas as pd

def analysis(file, user_id):
	times = 0
	minutes = 0

	df = pd.read_json('user_study.json')
	times = len(df[df['user_id'] == user_id])
	minutes = df[df['user_id'] == user_id]['minutes'].sum()

	return times, minutes
