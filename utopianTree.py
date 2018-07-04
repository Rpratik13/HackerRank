def utopianTree(n):
	height = 1
	for i in range(1,n+1):
		if i%2!=0:
			height *= 2
		else:
			height+=1
	return height

t = int(input())

for t_itr in range(t):
    n = int(input())

    result = utopianTree(n)

    print(result)