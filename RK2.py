def createDataPoints(x0,n,h):
	i=1
	x = []
	while i!=n+2:
		x.append(x0+(i-1)*h)
		i+=1
	return x

def func(x,y):
	ans = (y-1)**(0.5)
	return ans

def RK2(x,y,h):
	for i in range(0,len(x)-1):
		print("On [",end="")
		print(x[i],end=" ")
		print(",",end="")
		print(x[i]+h,end="")
		print("]")
		k1 = h*func(x[i],y[i])
		print("k1 = ",end="")
		print(k1)
		k2 = h*func(x[i]+h,y[i]+k1)
		print("k2 = ",end="")
		print(k2)
		yt = y[i]+(k1 + k2)/2
		print("y",end="")
		print(i+1,end=" ")
		print("=",end=" ")
		print(yt)
		y.append(yt)
	return y[len(y)-1]

pi = 3.141592654
x0 = int(input("Enter x0 = "))
y0 = int(input("Enter y0 = "))
xn = int(input("Enter xn = "))
n = int(input("Enter no. of sub-intervals: "))
h = (xn-x0)/n

x = createDataPoints(x0,n,h)
y = []
y.append(y0)
print(RK2(x,y,h))