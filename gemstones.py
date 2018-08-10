def checkgem(inp,x):
	for i in range(len(inp)):
		if x not in inp[i]:
			return False;
	return True;



def gemstones(inp):
	count = 0;
	for i in range(97,123):
		if checkgem(inp,chr(i)):
			count+=1;
	return count

n = int(input());

inp = [];
for i in range(n):
	s = input();
	inp.append(s);
print(gemstones(inp))