# Project Euler Solutions: Problem 097
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 02:26, 16 March 2020
# https://github.com/noicepollution/project-euler

val = 1
for i in range(1, 7830458):
	val = (val * 2) % (10000000000)
print((28433 * val + 1)% (10000000000))