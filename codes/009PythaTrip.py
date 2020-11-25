# Project Euler Solutions: Problem 009
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 15:56, 29 June 2015
# https://github.com/noicepollution/project-euler

# Function to return the hypotenuse of a given pair of lengths.
# With the sides and hypotenuse known, the next step is to check
# if the given pythagorean triple lengths add up to 1000. 

def check(x,y):
	for i in range(y+1,x+y):
		if i*i == (x*x+y*y):
			return i
	return -1
ch = 0
for i in range(1,400):
	for j in range(i+1,400):
		k = check(i,j)
		if k!=-1 and i+j+k==1000:
			print(i,j,k,i*j*k)
			ch = 1
			break
	if ch == 1:
		break
