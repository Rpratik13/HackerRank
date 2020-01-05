def beautifulBinaryString(n, s):
	count = int()
	for i in range(n - 2):
		if s[i:i + 3] == '010':
			s = str(int(s) + (10 ** (n - i - 3)))
			print(s)
			s = (n - len(s)) * '0' + s
			count += 1

	return count


if __name__ == '__main__':
	n = int(input())
	s = input()
	print(beautifulBinaryString(n, s))