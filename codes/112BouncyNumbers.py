# Project Euler Solutions: Problem 112
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 01:00, 24 October 2020
# https://github.com/noicepollution/project-euler

def isBouncy(num):
	nm = sorted(str(num))
	num = [i for i in str(num)]
	return not (nm == num or num == nm[::-1])

ct, num = 19602, 21780
while True:
	num += 1
	if isBouncy(num):
		ct += 1
		val = str(0.99 * num)
		if val[-2:] == '.0' and int(val[:-2]) == ct:
			break
print(num)