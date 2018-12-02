#!/usr/bin/env python3

import os
import os.path
import requests

def download(url):
	'''Download file and store to current directory from sepcified URL

	:arg url: The URL for file which should be downloaded
	'''
	req = requests.get(url)
	# Check the exists of file
	if req.status_code == 404:
		print('No such file found at %s' % url)
		return

	filename = url.split('/')[-1]
	with open(filename, 'wb') as fobj:
		fobj.write(req.content)
	print("Download over.")


if __name__ == '__main__':
	url = input('Enter a URL: ')
	download(url)