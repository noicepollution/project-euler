# Project Euler Solutions: Problem 092
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 23:44, 18 May 2017
# https://github.com/noicepollution/project-euler

def squareResult(x):
	s = 0
	while x>0:
		r = x%10
		x = x//10
		s = s+r**2
	return s
c = 0
for i in range(10000000,0,-1):
	n = squareResult(i)
	while(n not in [1,10,13,32,44,31,23]):
		if n in [85,89,145,42,20,4,16,37,58,154,541,514,451,415,2,61,98,40]:
			c = c+1
			break
		n = squareResult(n)
print(c)
