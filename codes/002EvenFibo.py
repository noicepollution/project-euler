# Project Euler Solutions: Problem 002
# Copyright (c) Project noicepollution. All Rights Reserved.
# Solution timestamp: 15:28, 20 June 2015
# https://github.com/noicepollution/project-euler

# f and s contain the current and next Fibonacci numbers.
# Setting an upper limit on the Fibonacci number as 4 million.

def fibo():
	sum = 0
	f = 1
	s = 2
	while f < 4000000:
		if f%2 == 0:
			sum += f
		(f,s) = (s,f+s)
	return sum

print(fibo())