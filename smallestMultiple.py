def factorial(n):
	if n==1:
		return 1
	else:
		return factorial(n-1)*n


def largestMultiple(n):
	max1 = factorial(n)
	t=n

	while t<=max1:
		a = 1
		count = 0
		while a <= n:
			if t%a==0:
				count+=1
			a+=1
			
		if count == n:
			return t

		t = t+n



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    result = largestMultiple(n)

    print(result)