# Project Euler Solutions: Problem 063
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 02:51, 16 March 2020
# https://github.com/noicepollution/project-euler

ctr = 0
for num in range(1, 10):
	j = 1
	flag = True
	while flag:
		nm_st = str(num ** j)
		if len(nm_st) == j:
			ctr += 1
		else:
			flag = False
		j += 1
print(ctr)