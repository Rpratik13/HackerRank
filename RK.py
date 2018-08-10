def createDataPoints(x0,n,h):
	i=1
	x = []
	while i!=n+2:
		x.append(x0+(i-1)*h)
		i+=1
	return x

def func(x,y):
	ans = (y**2-x**2)/(y**2+x**2)
	return ans

def RK4(x,y,h):
	
	for i in range(0,len(x)):
		k1 = h*func(x[i],y[i])
		k2 = h*func(x[i]+h/2,y[i]+k1/2)
		k3 = h*func(x[i]+h/2,y[i]+k2/2)
		k4 = h*func(x[i]+h,y[i]+k3)
		yt = (k1 + 2*k2 + 2*k3 + k4)/6
		y.append(yt)

	return y[len(y)-1]

def RK2(x,y,h):
	for i in range(0,len(x)):
		k1 = h*func(x[i],y[i])
		k2 = h*func(x[i]+h/2,y[i]+k1/2)
		yt = y[i]+(k1 + k2)/2
		y.append(yt)
	return y[len(y)-2]

x0 = int(input("Enter x0: "))
y0 = int(input("Enter y0: "))
xn = int(input("Enter xn: "))

n = int(input("Enter no. of sub-intervals: "))

h = (xn-x0)/n

x = createDataPoints(x0,n,h)
y = []
y.append(y0)
print(RK2(x,y,h))