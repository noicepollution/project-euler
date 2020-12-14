# Project Euler Solutions: Problem 037
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 22:59, 11 June 2017
# https://github.com/noicepollution/project-euler

def primecheck(x):
	if x%2==0 and x!=2 and x!=0:
		return False
	if x==1:
		return False
	i = 3
	while i*i<=x:
		if x%i==0:
			return False
		i = i+2
	return True

i = 23
c = 0
s = 0
while c!=11:
	if primecheck(i):
		l = 0
		r = i
		ch = 0
		e = 1
		while r>0:
			rem = r%10
			l = rem*e+l
			e = e*10
			r = r//10
			if not(primecheck(l) and primecheck(r)):
				ch = 1
		if ch==0:
			c = c+1
			s = s+i
			print(i,c,s)
	i = i+1
print(s)
