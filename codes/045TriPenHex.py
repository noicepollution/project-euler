# Project Euler Solutions: Problem 045
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 14:59, 15 March 2020
# https://github.com/noicepollution/project-euler

from math import sqrt, floor, ceil

def is_pentagonal(num):
	res = (1 + sqrt(1 + 4*3*2*num)) / (2*3)
	return floor(res) == ceil(res)

def is_hexagonal(num):
	res = (1 + sqrt(1 + 4*2*num)) / (2*2)
	return floor(res) == ceil(res)

i = 1 
nm = -1
while nm != 2:
	tri_nm = i * (i+1) // 2
	if is_pentagonal(tri_nm) and is_hexagonal(tri_nm):
		nm += 1
	i += 1
print(tri_nm)