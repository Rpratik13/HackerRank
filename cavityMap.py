def cavityMap(inp,n):
	for i in range(n):
		if i==0 or i==n-1:
			continue

		for j in range(n):
			if j == 0 or j == n-1:
				continue

			if inp[i][j-1]<inp[i][j] and inp[i][j+1]<inp[i][j]:
				inp[i][j]= -1
	return inp;



n = int(input());
inp = [];
for i in range(n):
	row = input();
	l = [];
	for j in range(len(row)):
		if row[j]==' ':
			l.append(-10);
		else:
			l.append(int(row[j]));
	inp.append(l);



result = cavityMap(inp,n);

for i in range(n):
	for j in range(len(result[i])):
		if result[i][j]==-1:
			print("X",end="");
		elif result[i][j]==-10:
			print(" ",end="")
		else:
			print(result[i][j], end="");
	print("")
