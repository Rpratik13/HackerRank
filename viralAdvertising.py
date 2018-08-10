def viralAdvertising(n):
	cumulative = 2
	liked = 2
	for i in range(2,n+1):
		liked *= 3

		if liked%2==0:
			cumulative += liked//2
			liked = liked//2
		else:
			cumulative +=(liked-1)//2
			liked = (liked-1)//2
	return cumulative

n = int(input())

result = viralAdvertising(n)

print(result)