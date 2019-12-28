def strangeCounter(t):
	time = 1
	inc = 3

	while time <= t:
		time += inc
		inc *= 2
	time -= inc // 2
	inc //= 2

	return inc - (t - time)


t = int(input())
print(strangeCounter(t))