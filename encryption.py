from math import sqrt,ceil,floor


def encryption(s):
	s = s.replace(' ','');
	row = floor(sqrt(len(s)));
	col = ceil(sqrt(len(s)));

	if((row*col)<len(s)):
		row = col;
	print(row);
	print(col);
	ans = ""

	i = 0;
	
	while(i<col):
		j = i;
		while(j<=len(s)-1):
			ans = ans + s[j];
			j = j + col;
		ans = ans + " ";
		i+=1;
	return ans;


s = input();

result = encryption(s);

print(result);
