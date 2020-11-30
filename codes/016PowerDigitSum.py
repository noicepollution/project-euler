# Project Euler Solutions: Problem 016
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 01:15, 17 May 2017
# https://github.com/noicepollution/project-euler

# Directly calculating 2^1000 and adding up the digits.
# Thanks to Python's lack of upper limits on numbers, this can be done directly.

def sumof(x):
	s = 0
	while x>0:
		r = x%10
		x = x/10
		s = s+r
	return(s)

print(sumof(2**1000))
