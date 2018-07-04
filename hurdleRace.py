def hurdleRace(k,height):
	max1 = max(height)
	if max1<=k:
		return 0
	else:
		return (max1-k)

nk = input().split()

n = int(nk[0])

k = int(nk[1])

height = list(map(int, input().rstrip().split()))

result = hurdleRace(k, height)

print(result)