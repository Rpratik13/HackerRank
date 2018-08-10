def func(x):
	ans = 2*x-3
	return ans

def bisection(a,b,tol):
	temp = 913023

	if func(a)*func(b)<0:
		x = (a + b)/2
		print(a,end ="\t \t")
		print(func(a),end="\t \t")
		print(b,end="\t\t")
		print(func(b),end="\t \t")
		print(x,end="\t \t")
		print(func(x))
		if func(x)>0:
			a=x
		else:
			b=x	

		while(abs(temp-x)>tol):
			temp = x
			x = (a + b)/2
			
			if func(x)>0:
				a=x
			else:
				b=x	
			print(a,end ="\t\t")
			print(func(a),end="\t\t")
			print(b,end="\t\t")
			print(func(b),end="\t\t")
			print(x,end="\t\t")
			print(func(x))
		temp = x
		x = (a + b)/2
		
		if func(x)>0:
			a=x
		else:
			b=x	
		print(a,end ="\t\t")
		print(func(a),end="\t\t")
		print(b,end="\t\t")
		print(func(b),end="\t\t")
		print(x,end="\t\t")
		print(func(x))
	
		return x
	
			
	else:
		return False


a = int(input())
b = int(input())
error = int(input())
error = -1*error
if func(a)<func(b):
	t = a 
	a = b
	b = t

tol = 0.5 * (10**error)
print("a \t \t f(a) \t \t b \t \t f(b) \t \t x \t \t f(x)")

ans = bisection(a,b,tol)
if ans == False:
	print("f(a)*f(b)>=0")
else:
	print("Required root is ",end="")
	print(ans)

