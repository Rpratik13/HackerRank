def sequenceEquation(n, inp):
	ans = list()
	for i in range(1, n + 1):
		x = inp.index(i) + 1
		ans.append(inp.index(x) + 1)
	return ans

if __name__ == '__main__':
	n = int(input())
	inp = [int(i) for i in input().split()]
	for i in sequenceEquation(n, inp):
		print(i)