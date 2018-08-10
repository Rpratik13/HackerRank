def findDigits(n):
	temp = n
	count = 0
	while temp!=0:
		d = temp%10
		if d == 0:
			temp = temp//10
			continue
		if n%d==0:
			count+=1
		temp = temp//10

	return count



t = int(input())

for t_itr in range(t):
	n = int(input())

	result = findDigits(n)

	print(result)