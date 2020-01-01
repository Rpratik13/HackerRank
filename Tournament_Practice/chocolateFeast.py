def chocolateFeast(n, c, m):
	chocolates = n // c
	wrappers = n // c

	while wrappers >= m:
		chocolates += wrappers // m
		wrappers = (wrappers // m) + (wrappers % m)
	return chocolates

if __name__ == '__main__':
	t = int(input())
	for test in range(t):
		ncm = [int(inp) for inp in input().split()]
		n = ncm[0]
		c = ncm[1]
		m = ncm[2]
		print(chocolateFeast(n, c, m))
