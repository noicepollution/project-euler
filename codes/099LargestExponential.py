# Project Euler Solutions: Problem 099
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 11:56, 04 June 2020
# https://github.com/noicepollution/project-euler

from math import log

max_val, line_no = 0, 0
with open("problem99.txt") as file_data:
	ln_no = 0
	for line in file_data.readlines():
		ln_no += 1
		line = line.split(",")
		line = [int(i.strip()) for i in line]
		res = line[1] * log(line[0])
		if res > max_val:
			max_val, line_no = res, ln_no
print(line_no)
