#!/bin/python3

import sys

def lowestTriangle(base, area):
    height = (2*area)/base
    height = height//1

    while (base*height)/2>=area:
    	height-=1
    return (height+1)//1


base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(int(roung(height))