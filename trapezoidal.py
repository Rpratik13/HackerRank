def func(x):
	ans = x
	return ans


def trapazoidal(x,h,n):
	sum1 = 0
	for i in range(1,len(x)-1):
		sum1 += 2*(x[i])
	sum1+=x[0]+x[len(x)-1]
	return (h/2)*sum1


a = int(input("Enter lower integration limit: "))
b = int(input("Enter upper integration limit: "))
n = int(input("Enter no. of sub-intervals: "))

h = (b-a)/n
x = []

i = 1

while i!=n+2:
	x.append(a+(i-1)*h)
	i+=1

print(trapazoidal(x,h,n))