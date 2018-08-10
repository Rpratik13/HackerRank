def hrInString(s):
	hr = ['h','a','c','k','e','r','r','a','n','k'];
	i = 0;

	for k in range(len(s)):
		if s[k] == hr[i]:
			i+=1;
		if i == 10:
			break

	if i==10:
		return "YES";
	else:
		return "NO";

n = int(input());
for i in range(n):
	s = input();

	print(hrInString(s));
