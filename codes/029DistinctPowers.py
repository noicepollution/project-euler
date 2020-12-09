# Project Euler Solutions: Problem 029
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 01:05, 17 May 2017
# https://github.com/noicepollution/project-euler

li = []
for a in range(2,101):
	for b in range(2,101):
		n = a**b
		if n not in li:
			li.append(n)
			li.sort()
print(len(li))
