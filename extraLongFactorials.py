def extraLongFactorials(n):
	if n == 1:
		return 1
	else:
		return n*extraLongFactorials(n-1)



n = int(input())

result = extraLongFactorials(n)

print(result)