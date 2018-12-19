#!/usr/bin/env python3

import os
import sys

def parse_file(path):
	'''
	Analyse the specific file, return its information such as space、tab symbol、line etc
	: arg path: the path of text file 
	: return: a tuple that include number of space、tab、line
	'''
	fd = open(path)
	i = 0
	spaces = 0
	tabs = 0
	for i, line in enumerate(fd):
		spaces += line.count(' ')
		tabs += line.count('\t')
	# close the file
	fd.close()

	# return a tuple
	return spaces, tabs, i + 1


def main(path):
	'''
	Function for printing the result of file analysis
	: arg path: the path of file to analyse
	: return: if exists -> True, else False
	'''
	if os.path.exists(path):
		spaces, tabs, lines = parse_file(path)
		print("Spaces {}. tabs {}. lines {}".format(spaces, tabs, lines))
		return True
	else:
		return False


if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		sys.exit(-1)
		sys.exit(0)



