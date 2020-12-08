# Project Euler Solutions: Problem 026
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 18:23, 20 June 2017
# https://github.com/noicepollution/project-euler

n = 1000
rem = []
for i in range(999,0,-1):
	e = 1
	ch = 0
	while True:
		r = e%i
		if r not in rem:
			rem.append(r)
			e = r*10
		else:
			x = len(rem)
			if x == i-1:
				print(i)
				ch = 1
			rem.clear()
			break
	if ch==1:
		break