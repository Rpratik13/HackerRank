def interpolation(n,x,y):
	ans = 0
	for i in range(0,len(x)):
		sum1 = 1
		sum2 = 1

		for j in range(0,len(x)):
			if i==j:
				continue
			else:
				sum1 = sum1 * (n-x[j])
				sum2 = sum2 * (x[i]-x[j])
				
		ans = ans + (sum1/sum2)*y[i]

	return ans


n = float(input())
y = [500,653,945,1248,1400]
x = [1.25,1.08,0.84,0.60,0.50]

result = interpolation(n,x,y)

print(result)