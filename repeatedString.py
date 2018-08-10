#!/bin/python3

import math
import os
import random
import re
import sys

def repeatedString(s, n):
	count = s.count('a')
	a = count * (n//len(s))
	
	temp = n-(len(s)*(n//len(s)))
	temp_s = s[:temp]
	a += temp_s.count('a')
	return a


s = input()

n = int(input())

result = repeatedString(s, n)

print(result)