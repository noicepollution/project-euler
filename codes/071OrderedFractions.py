# Project Euler Solutions: Problem 071
# Copyright (c) noicepollution. All Rights Reserved.
# Solution timestamp: 13:41, 23 March 2020
# https://github.com/noicepollution/project-euler

threshold_nm, threshold_dm = 3, 7
fin_nm, fin_dm = 0, 1
for dm in range(1000000, 1, -1):
	nm = (threshold_nm * dm - 1)// threshold_dm
	if (nm * fin_dm) > (dm * fin_nm):
		fin_nm, fin_dm = nm, dm
print(fin_nm)    