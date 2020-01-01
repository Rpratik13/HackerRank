def superReducedString(s):
	i = 0
	while i < len(s) - 1:
		if s[i] == s[i + 1]:
			s = s[:i] + s[i + 2:]
			i = 0
		else:
			i += 1

	if len(s) == 0:
		return 'Empty String'
	else:
		return s


if __name__ == '__main__':
	s = input()
	print(superReducedString(s))