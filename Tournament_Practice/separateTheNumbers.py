def separateTheNumbers(s):
	for i in range(1, len(s)):
		ans = s[:i]
		current = i
		nxt = int(ans) + 1
		while int(s[current:current + len(nxt)]) + 1 == nxt:



if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		x = input()
		print(separateTheNumbers(x))