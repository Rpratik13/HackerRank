def checkPangram(s):
	check = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
	ans = []

	for i in range(len(s)):
		if s[i] in ans:
			continue

		if s[i].isalpha():
			ans.append(s[i]);

	ans.sort()
	if ans==check:
		return "pangram"
	else:
		return "not pangram"


s = input();

print(checkPangram(s.lower()));