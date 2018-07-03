def countApplesAndOranges(s,t,a,b,apples,oranges):
	count_apples=count_oranges=0
	result = []
	for i in apples:
		if (a+i)  in range(s,t+1):
			count_apples+=1 
	for i in oranges:
		if (b+i) in range(s,t+1):
			count_oranges+=1 
	result.append(count_apples)
	result.append(count_oranges)
	return result

st = input().split()

s = int(st[0])

t = int(st[1])

ab = input().split()

a = int(ab[0])

b = int(ab[1])

mn = input().split()

m = int(mn[0])

n = int(mn[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

result = countApplesAndOranges(s, t, a, b, apples, oranges)

for i in result:
	print(i)