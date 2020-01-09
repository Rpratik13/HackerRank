 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
	count = 0
	a_sqrt = int(math.sqrt(a))
	b_sqrt = int(math.sqrt(b)) + 1
	for i in range(a_sqrt, b_sqrt):
		if i ** 2 in range(a, b + 1):
			count += 1
	return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
