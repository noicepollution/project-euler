# Project Euler Solutions: Problem 004
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 20:53, 20 June 2015
# https://github.com/noicepollution/project-euler

# A function to check whether a given number is a palindrome or not.
# Iterate through the combinations of three digit numbers and check if
# it satisfies the condition.
def palincheck(x):
	x = str(x)
	if x == x[::-1]:
		return True
	return False

def ans():
	co = 0
	for i in range(999,100,-1):
		for j in range(i-1,99,-1):
			if i*j>co:
				if palincheck(i*j):
					if i*j>co:
						co = i*j
	return co
print(ans())
