def collatz(n):
	while n != 1:
		if n % 2 == 0:
			n //= 2
		else:
			n = 3 * n + 1

	return True


if __name__ == '__main__':
	for i in range(1, 10000):
		print("{}: ".format(i) + str(collatz(i)))