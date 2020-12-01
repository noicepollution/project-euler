# Project Euler Solutions: Problem 018
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 16:53, 11 June 2017
# https://github.com/noicepollution/project-euler

# This is solved using a bottom-up approach.
# For each value in the penultimate row, calculate the maximum possible sum.
# Iterate to the previous row, and add the current row element value to maximum element value.
# After doing so, iterate back to the row above and perform the same.
# Continue doing the same until the 0th row is reached, which will contain the maximum path sum. 

rows = []
f = open('problem18')
for line in f:
	rows.append([int(i) for i in line.rstrip('\n').split(" ")])
for i in range(len(rows)-2,-1,-1):
	for j in range(len(rows[i])):
		rows[i][j] = rows[i][j]+max(rows[i+1][j],rows[i+1][j+1])
	if i==0:
		print(rows[0])
