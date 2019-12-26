def factorial(n):
	if n < 2:
		return 1;
	return n * factorial(n-1);

def factorialDigitSum(n):
	sm = 0;
	while n:
		sm += (n % 10);
		n //= 10;
	return sm;

def main():
	inp = int(input());
	print(factorialDigitSum(factorial(inp)));

if __name__ == '__main__':
	main();
