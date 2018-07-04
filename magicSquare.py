def formingMagicSquare(s):
	a = [
	[[8,1,6],[3,5,7],[4,9,2]],
	[[8,3,4],[1,5,9],[6,7,2]],
	[[4,3,8],[9,5,1],[2,7,6]],
	[[4,9,2],[3,5,7],[8,1,6]],
	[[2,9,4],[7,5,3],[6,1,8]],
	[[2,7,6],[9,5,1],[4,3,8]],
	[[6,7,2],[1,5,9],[8,3,4]],
	[[6,1,8],[7,5,3],[2,9,4]]
	]

	k = 0 
	min1 = 10000
	while k < 8:
		diff = 0
		for i in range(0,3):
			for j in range(0,3):
				diff = diff + abs(a[k][i][j]-s[i][j])
		if diff<min1:
			min1=diff
		k+=1

	return min1	

s = []

for i in range(3):
    s.append(list(map(int, input().rstrip().split())))

result = formingMagicSquare(s)

print(result)