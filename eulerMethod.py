import math

def func(x,y):
	return (y+x)**2

pi = 3.14159

a = 0
b = pi/2

h = (b-a)/2

x = 0
y = -1

while x!=b:
	y = y + h*func(x,y)
	x+=h

print(y)
print(-pi/2 + math.tan((pi/2)-(pi/4)))