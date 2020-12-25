# Project Euler Solutions: Problem 055
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 23:57, 16 March 2020
# https://github.com/noicepollution/project-euler

lych_count = 9999
for i in range(1, 10000):
	iters, new_num = 0, i
	# new_num = i
	while iters < 50:
		new_num = new_num + int(str(new_num)[::-1])
		if str(new_num) == str(new_num)[::-1]:
			lych_count -= 1
			break
		iters += 1
print(lych_count)