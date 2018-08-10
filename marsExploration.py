def checkSOS(s):
	count = 0;

	if s[0]!='S':
		count+=1;
	if s[1]!='O':
		count+=1;
	if s[2]!='S':
		count+=1;

	return count;

def marsExploration(s):
	ans = 0;
	while s != '':
		check = s[:3];
		ans += checkSOS(check);
		s = s[3:];
	return ans

s = input();
result = marsExploration(s);
print(result);