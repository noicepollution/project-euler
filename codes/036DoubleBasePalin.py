# Project Euler Solutions: Problem 036
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 23:10, 11 June 2017
# https://github.com/noicepollution/project-euler

s = 0
for i in range(1,1000000):
	a = str(i)
	b = a[::-1]
	c = bin(i)
	c = c[2:]
	d = c[::-1]
	if a==b and c==d:
		print(i)
		s = s+i
print(s)
