# Project Euler Solutions: Problem 005
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 21:12, 20 June 2015
# https://github.com/noicepollution/project-euler

# The simplest answer is to calculate the least common multiple of the numbers
# from 2 to 20. This is the smallest possible number that satisfies the condition.

def lcm(x,y):
	m,n = x,y
	if m < n:
		(m,n)=(n,m)
	while (m%n) != 0:
		(m,n) = (n,m%n)
	return ((x*y)//n)

c = 1
for i in range(2,21):
	c = lcm(c,i)
print(c)
