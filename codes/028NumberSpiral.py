# Project Euler Solutions: Problem 028
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 18:45, 20 June 2017
# https://github.com/noicepollution/project-euler

s = 1
for i in range(1001,2,-2):
	m = i**2
	s = s+m
	print(m)
	for j in range(0,3):
		m = m-i+1
		s = s+m
print(s)
