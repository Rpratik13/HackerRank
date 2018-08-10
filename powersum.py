def powerSum(X, N, count):
	if count<((X**0.5)+1):
		if X<0:
			return 0
		elif X==0:
			return 1
		if (X-(count**N))>=0:
			return powerSum(X-(count**N),N,count+1)+powerSum(X,N,count+1)
		else:
			return powerSum(X,N,count+1)

	return 0


X = int(input())

N = int(input())

count = 1

result = powerSum(X, N,count)

print(result)


