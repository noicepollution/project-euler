# Project Euler Solutions: Problem 079
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 00:33, 17 March 2020
# https://github.com/noicepollution/project-euler

from collections import OrderedDict

next_nms = {}
f = open('problem79.txt')
for line in f:
	for i in range(0, len(line)):
		if line[i] != '\n':
			lst = next_nms[line[i]] if line[i] in next_nms.keys() else []
			res = [j for j in line[i+1:] if j != '\n']
			lst = set(lst).union(set(res))
			lst = list(lst)
			next_nms[line[i]] = lst

ordered_d = OrderedDict(sorted(next_nms.items(), key=lambda x: len(x[1])))

passcode = ''
for i in ordered_d.keys():
	passcode = str(i) + passcode
	print(i, ordered_d[i])
print(passcode)