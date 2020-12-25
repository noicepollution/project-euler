# Project Euler Solutions: Problem 057
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 23:18, 17 March 2020
# https://github.com/noicepollution/project-euler

from fractions import Fraction

ctr = 0
fr1 = Fraction(1,1)
for i in range(1, 1000):
	fr1 = Fraction(1,1) + Fraction(1, (Fraction(1,1) + fr1))
	if len(str(fr1.numerator)) > len(str(fr1.denominator)):
		ctr += 1
print(ctr)