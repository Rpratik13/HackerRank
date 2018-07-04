import math

def square(n):
	return n*n


def distance(x,y):

	result = math.sqrt(square(x[0]-y[0])+square(x[1]-y[1])) 

	return result


x = list(map(int, input().rstrip().split()))

y = list(map(int, input().rstrip().split()))


print(distance(x,y))


