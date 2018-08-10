def halloweenSale(p,d,m,s):
	count = 0;
	while(p<=s):
		count+=1;
		s -= p;
		if (p-d>m):
			p-=d;
		else:
			p=m;
	return count;


inp = [int(x) for x in input().split()];

p = inp[0];
d = inp[1];
m = inp[2];
s = inp[3];

result = halloweenSale(p,d,m,s);
print(result);