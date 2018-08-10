import math

def func(x,y):
	return (y-1)**(0.5)


pi = 3.14159

a = 0
b = 2

h = (b-a)/4
x = 0
y = 5

while x!=b:
	y1 = y + h*func(x,y)
	print(y1)
	y  = y + (h/2)*(func(x,y)+func(x+h,y1))
	print(y)
	x+=h
