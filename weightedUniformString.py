def weightedUniformString(s):
	ans = [];
	chars = [];
	check_val  = 0;
	mul = 1;
	check_char = '';

	for i in range(len(s)):
		if (s[i] in chars) and s[i]==s[i-1]:
			mul+=1;
			ans.append((ord(s[i])-96)*mul)
		else:
			ans.append(ord(s[i])-96);
			chars.append(s[i]);
			check_char = s[i];
			check_val = s[i];
			mul = 1;
	return ans


s = input();

n = int(input());

result = weightedUniformString(s);


for i in range(n):
	val = int(input());

	if val in result:
		print("Yes");
	else:
		print("No");