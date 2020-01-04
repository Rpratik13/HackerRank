def func(n):
	while n < 10:
		n += 2
		if n % 2 == 0:
			break
	else:
		print('yay')


func(int(input()))	