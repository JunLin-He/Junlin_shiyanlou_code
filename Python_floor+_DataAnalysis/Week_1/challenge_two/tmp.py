import sqlite3
import pandas as pd

def convert(file,user_id):
	sql_con = sqlite3.connect(file) #connect to database
	sql_query = "SELECT SUM(minutes),count(*) FROM data WHERE user_id is not null AND user_id == " + str(user_id)  #situation for query 

	sumdata = pd.read_sql(sql_query,sql_con) #execute read command.
  
	ifexist = int(sumdata['count(*)'].tolist()[0])
	if ifexist == 0:
		#print(sumdata.empty)
		return ifexist
	else:
		sum_minutes = int(sumdata['SUM(minutes)'].tolist()[0])
		return sum_minutes
  
s_m = convert("users_data.sqlite",2) #for test
print(s_m)