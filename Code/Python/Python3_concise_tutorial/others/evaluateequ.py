#!/usr/bin/env python3

#x = 0
sum = 0
'''
while(x < 10):
	x += 1
	sum = 1 / x + sum

print(sum)
'''
for i in range(1, 11):
	sum += 1.0 / i
	print("{:2d} {:6.4f}".format(i, sum))

