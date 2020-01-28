def checkPangram(s):
	check = [False] * 26

	for i in range(len(s)):
		if s[i].isalpha():
			check[ord(s[i]) - 97] = True


	if all(check):
		return "pangram"
	else:
		return "not pangram"


s = input();

print(checkPangram(s.lower()));