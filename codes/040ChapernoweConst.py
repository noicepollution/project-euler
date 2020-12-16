# Project Euler Solutions: Problem 040
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 12:15, 15 March 2020
# https://github.com/noicepollution/project-euler

i = 1
num_st = ""
while len(num_st) < 1000002:
	num_st = num_st + str(i)
	i += 1
print(int(num_st[0]) * int(num_st[9]) * int(num_st[99]) * int(num_st[999]) * 
	  int(num_st[9999]) * int(num_st[99999]) * int(num_st[999999]))