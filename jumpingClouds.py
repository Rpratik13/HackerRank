def jumpingOnClouds(c, k):
	e = 100
	i = 0
	check = True
	while(i != 0 or check):
		i = (i + k) % len(c)
		if c[i]:
			e -= 3
		else:
			e -= 1

		if i == 0:
			check = False
	return e


nk = input().split()

n = int(nk[0])

k = int(nk[1])

c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c, k)

print(result)