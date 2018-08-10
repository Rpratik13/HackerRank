from math import sqrt,ceil;

def checkPrime(n):
	if n == 2: 
		return True;
	
	if n % 2 == 0 or n == 1:
		return False;

	for i in range(3,ceil(sqrt(n))+1):
		if n % i == 0:
			return False;
	return True;

def positionPrime(position):
	pos = 1;
	x = 3;
	if position == 1:
		return 2;
	while (pos != position):
		if checkPrime(x):
			pos += 1;
		x += 2;
	return x-2;

def suff(n):
	if (n % 100) > 10 and (n % 100) < 20:
		return "th";
	elif (n % 10) == 1:
		return "st";
	elif (n % 10) == 2:
		return "nd";
	elif (n % 10) == 3:
		return "rd";
	else:
		return "th";

inp = int(input(E"nter required no. of Prime Number: "));
print("The {}{} Prime Number is {}.".format(inp,suff(inp),positionPrime(inp)));
