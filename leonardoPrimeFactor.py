from math import ceil, sqrt

def isPrime(n):
	val = ceil(sqrt(n))
	if n == 2:
		return True
	if n % 2 == 0 or n == 1:
		return False
	i = 3
	while(i < val):
		if n % i == 0:
			return False;
		i += ;
	return True

def primeFactors(inp):
	ans = []
	for i in inp:
		count_prime=0
		for j in range(2, i + 1):
			if isPrime(j) and i % j == 0:
				count_prime += 1
		ans.append(count_prime)
	return ans


count = int(input());
inp = [int(x) for x in input().split()]

result = primeFactors(inp)

print(result)