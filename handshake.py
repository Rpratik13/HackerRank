#!/bin/python3

import os
import sys

def handshake(n):
    sum1 = 0
    for i in range(n-1,0,-1):
        sum1 += i
    return sum1
    
t = int(input())

for t_itr in range(t):
    n = int(input())

    result = handshake(n)

    print(result)