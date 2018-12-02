#!/usr/bin/env python3

import sys

def Hours(minutes):
	hours, new_minutes = divmod(minutes, 60)
	return hours, new_minutes

def main():
	try:
		minutes = int(sys.argv[1])
	except Exception as e:
		print("Argument must be integer")
		exit(-1)

	if minutes <= 0:
		print("ValueError： Input number cannot be  negative")
		sys.exit(-1)
	else:
		hours, new_minutes = Hours(minutes)
		print("{} H, {} M".format(hours, new_minutes))


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Wrong input.")
		print("Usage: ./MinutesToHours.py <Minutes>")
	else: 
		main()
