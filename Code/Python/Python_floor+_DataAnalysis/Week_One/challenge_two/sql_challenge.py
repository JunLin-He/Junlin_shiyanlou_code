""" Package dependency: pandas
"""
import sqlite3
import pandas as pd

def count(file, user_id):
	sql_con = sqlite3.connect(file)
	sql_query = "SELECT SUM(minutes) FROM data WHERE user_id = " + user_id
	df_sum_minutes = pd.read_sql(sql_query, sql_con)
	try:
		sum_minutes = int(df_sum_minutes.iat[0, 0])
	except TypeError:
		sum_minutes = 0
	sql_con.close()
	return sum_minutes

sum_min = count("users_data.sqlite", "123123412412412")	# Test case
print(sum_min)
