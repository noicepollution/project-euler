# Project Euler Solutions: Problem 052
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 01:58, 16 March 2020
# https://github.com/noicepollution/project-euler

i = 1
while True:
	j = 2
	nm_set = set(str(i))
	flag = 0
	while j < 7:
		set_nm = set(str(i*j))
		if len(set_nm - nm_set) > 0:
			flag = 1
			break
		set_nm.clear()
		j += 1
	if flag == 0:
		print(i)
		break
	i += 1