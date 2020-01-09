#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
def stringConstruction(s):
	alpha = []
	for i in s:
		if i not in alpha:
			alpha.append(i)
	alpha = set(alpha)
	return len(alpha)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
