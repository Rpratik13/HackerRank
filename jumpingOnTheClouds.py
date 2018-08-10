#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
	position = 0
	jump = 0	
	change = 0
	while position!=len(c)-1:
		if position+2<len(c):
			if c[position+2]==0:
				position += 2
				jump += 1
				change = 1
		if change==0:
			position+=1
			jump+=1
		change = 0
	return jump


n = int(input())

c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c)

print(result)