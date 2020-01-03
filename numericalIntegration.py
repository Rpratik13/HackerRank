def func(x):
	ans = x
	return ans


def trapazoidal(x,h,n):
	sum1 = 0
	for i in range(1,len(x)-1):
		sum1 += 2*(x[i])
	sum1+=x[0]+x[len(x)-1]
	return (h/2)*sum1

def simpson1(x,h,n):
	if n%2==0:	
		sum1 = 0
		for i in range(1,len(x)-1):
			if(i%2!=0):
				sum1 += 4*(x[i])
			else:
				sum1 += 2*(x[i])
		sum1+=x[0]+x[len(x)-1]
		return (h/3)*sum1
	else:
		return "Enter appropriate number of sub-intervals."

def simpson3(x,h,n):
	if n%3==0:
		sum1 = 0
		for i in range(1,len(x)-1):
			if(i%3!=0):
				sum1 += 2*(x[i])
			else:
				sum1 += 3*(x[i])
		sum1+=x[0]+x[len(x)-1]
		return (3*h/8)*sum1
	else:
		return "Enter appropriate number of sub-intervals."



a = int(input("Enter lower integration limit: "))
b = int(input("Enter upper integration limit: "))
n = int(input("Enter no. of sub-intervals: "))

h = (b-a)/n
x = []

i = 1

while i!=n+2:
	x.append(a+(i-1)*h)
	i+=1

print(simpson3(x,h,n))