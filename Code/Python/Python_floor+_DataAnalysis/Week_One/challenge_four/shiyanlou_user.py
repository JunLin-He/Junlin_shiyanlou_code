""" Package dependency: requests, lxml
"""

import requests
from lxml import html

def user_info(user_id):
	""" Collect the user_name/user_level/join_date of the shiyanlou user
	"""
	content = requests.get('https://www.shiyanlou.com/user/' + user_id)
	if content.status_code == 200:
		tree = html.fromstring(content.text)
		# get user_name
		user_name = str(tree.xpath("//span[@class='username']/text()")[0])
		# get user_level
		try:
			user_level = int(tree.xpath("//span[@class='user-level']/text()")[0][1:])
		except TypeError:
 			user_level = 0
		# get join_date
		join_date = str(tree.xpath("//span[@class='join-date']/text()")[0][:10])
		return user_name, user_level, join_date
	else:
		user_name = None
		user_level = None
		join_date = None
		return user_name, user_level, join_date


a = user_info("3")		# Test case
print(a)
