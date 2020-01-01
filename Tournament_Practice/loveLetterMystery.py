def loveLetterMystery(s):
	ans = 0
	first = s[:len(s) // 2]
	last = s[len(s) // 2:]
	if len(s) % 2 != 0:
		last = last[1:]
	

	for i, j in zip(first, last[::-1]):
		ans += abs(ord(i) - ord(j))

	return ans


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		s = input()
		print(loveLetterMystery(s))