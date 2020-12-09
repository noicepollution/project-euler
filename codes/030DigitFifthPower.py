# Project Euler Solutions: Problem 030
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 01:49, 17 May 2017
# https://github.com/noicepollution/project-euler

def fifthpower(x):
	n = x
	su = 0
	while x>0:
		r = x%10
		x = x/10
		su = su+(r**5)
	if n==su:
		print(n)
		return True
	else:
		return False

s = 0
for i in range(2,400000):
	if fifthpower(i):
		s = s+i
print(s)
