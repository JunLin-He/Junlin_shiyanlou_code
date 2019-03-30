import pandas as pd

def clean():
	# 构造所需数据的DataFrame
	df = pd.read_csv('earthquake.csv')
	new_df = df.loc[:, 'time':'mag']
	new_df['region'] = df['place'].str.split(',', expand=True)[1]
	df_clean = new_df.dropna()
	return df_clean    # Return the final DataFrame

def mag_region():
	df_clean = clean()	# 得到清洁后的数据

	### code ###

	return df_final	# 返回处理得到的 DataFrame