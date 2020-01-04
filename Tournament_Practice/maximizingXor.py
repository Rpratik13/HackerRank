def maximizingXor(m, n):
	ans = 0
	for i in range(m, n + 1):
		for j in range(m, n + 1):
			ans = max(ans, i ^ j)
	return ans

if __name__ == '__main__':
	m = int(input())
	n = int(input())
	print(maximizingXor(m, n))