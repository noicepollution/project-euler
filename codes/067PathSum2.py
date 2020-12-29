# Project Euler Solutions: Problem 067
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 16:55, 11 June 2017
# https://github.com/noicepollution/project-euler

rows = []
f = open('problem67')
for line in f:
	rows.append([int(i) for i in line.rstrip('\n').split(" ")])
for i in range(len(rows)-2,-1,-1):
	for j in range(len(rows[i])):
		rows[i][j] = rows[i][j]+max(rows[i+1][j],rows[i+1][j+1])
	if i==0:
		print(rows[0])
