""" Package dependence: pandas, tables
"""
import pandas as pd

def convert(file):
	""" Convert 0~1000 line data of users_data.json to a HDF5 file user_study.h5
	"""
	df = pd.read_json(file)
	df[:1000].to_hdf("user_study.h5", key="data", format="table")

convert("users_data.json")	# Test case
