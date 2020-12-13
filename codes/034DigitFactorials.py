# Project Euler Solutions: Problem 034
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 18:46, 04 June 2017
# https://github.com/noicepollution/project-euler

factorials = [1]
vl = 1
for i in range(1, 10):
	vl = vl * i
	factorials.append(vl)
res = 0
for i in range(10, 2540161):
	fact_sum = 0
	for j in str(i):
		fact_sum = fact_sum + factorials[int(j)]
	if fact_sum == i:
		res += i
print(res)