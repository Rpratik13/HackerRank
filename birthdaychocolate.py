def solve(s,d,m):
	i=0
	count=0
	while i < len(s)-m+1:
		sum1=0
		for j in range(0,m):
			sum1 += s[i+j]
		if sum1 == d:
			count+=1
			i+=1
	return count


n = int(input())

s = list(map(int, input().rstrip().split()))

dm = input().split()

d = int(dm[0])

m = int(dm[1])

result = solve(s, d, m)

print(result)