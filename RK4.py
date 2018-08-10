def createDataPoints(x0,n,h):
	i=1
	x = []
	while i!=n+2:
		x.append(x0+(i-1)*h)
		i+=1
	return x

def func(x,y):
	ans = (y-1)**0.5
	return ans

def RK4(x,y,h):
	for i in range(0,len(x)-1):
		print("On [",end="")
		print(x[i],end=" ")
		print(",",end="")
		print(x[i]+h,end="")
		print("]")
		k1 = h*func(x[i],y[i])
		print("k1 = ",end="")
		print(k1)
		k2 = h*func(x[i]+h/2,y[i]+k1/2)
		print("k2 = ",end="")
		print(k2)
		k3 = h*func(x[i]+h/2,y[i]+k2/2)
		print("k3 = ",end="")
		print(k3)
		k4 = h*func(x[i]+h,y[i]+k3)
		print("k4 = ",end="")
		print(k3)
		yt = y[i]+(k1 + 2*k2 + 2*k3+k4)/6
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
print(RK4(x,y,h))