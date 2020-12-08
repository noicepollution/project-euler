# Project Euler Solutions: Problem 027
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 21:00, 16 March 2020
# https://github.com/noicepollution/project-euler

def check(x):
	i = 2
	while i<=x//i:
		if x%i==0:
			return False
		i = i+1
	return True

max_ctr, res = 0, 0
for a in range(-1000, 1001):
	for b in range(-1000, 1001):
		if check(b):
			n = 0
			while check(abs(n**2 + a*n + b)):
				n += 1
			if n > max_ctr:
				max_ctr = n
				res = a*b
print(res)