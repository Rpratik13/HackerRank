#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    w.sort()
    cont = 1
    start = w[0]
    while len(w):
        if w[0] in range(start, start + 5):
            w.remove(w[0])
        else:
            start = w[0]
            cont += 1
    return cont


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
