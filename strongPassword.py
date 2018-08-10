def special(pw):
	sp_char = "!@#$%^&*()-+";
	for i in range(len(pw)):
		for j in range(len(sp_char)):
			if pw[i]==sp_char[j]:
				return True;

	return False;

def minimumNumber(n,pw):
	u=l=n=s=0;	
	for i in range(len(pw)):
		if pw[i].isupper():
			u = 1;
		elif pw[i].islower():
			l = 1;
		elif pw[i].isnumeric():
			n = 1;
		elif special(pw):
			s = 1;
	ss = u+l+n+s;

	if len(pw)<6:
		return 4-ss+(6-len(pw))-1;
	
	return 4-ss;

n = int(input());

pw = input();

result = minimumNumber(n,pw);

print(result);