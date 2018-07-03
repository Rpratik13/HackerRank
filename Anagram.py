import math
import os
import random
import re
import sys

def anagram(s):
	if len(s)%2 != 0:
		return -1
	else:
		length = len(s)
		str1 = s[:length//2]
		str2 = s[length//2:]
		for i in range(len(str1)):
			for j in range(len(str2)):
				if str1[i] == str2[j]:
					temp_str = str2[:j]
					temp_str2 = str2[j+1:]
					str2 = temp_str + temp_str2
					break
	
		return len(str2)


q = int(input())

for q_itr in range(q):
	s = input()
	result = anagram(s)
	print(result)