def largestMultiple(n):
	if n < 2:
		return n
	ans = inc = n * (n - 1)
	for num in range(n - 1, 1, -1):
		while ans % num != 0:
			ans += inc
		inc = ans
	return ans


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    result = largestMultiple(n)

    print(result)