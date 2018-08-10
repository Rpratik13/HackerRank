import math
import os
import random
import re
import sys


def funnyString(s):
    rev = s[::-1]
    list1 = []
    list2 = []
    for i in range(len(s) - 1):
        list1.append(abs(ord(s[i]) - ord(s[i + 1])))
        list2.append(abs(ord(rev[i]) - ord(rev[i + 1])))

    for j in range(len(list1)):
        if list1[j] != list2[j]:
            return 0

    return 1


num = int(input())

for q_itr in range(num):
    input_string = input()

    result = funnyString(input_string)
    if(result):
        print("Funny")
    else:
        print("Not Funny")
