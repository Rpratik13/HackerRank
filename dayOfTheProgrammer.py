def checkJulianLeap(year):
	if year%4==0:
		return True
	else: 
		return False

def checkGeorgianLeap(year):
	if year%400==0:
		return True
	elif year%100==0: 
		return False
	elif year%4==0:
		return True

def solve(year):
	if year == 1918:
		return("26.09." + str(year))
	elif year < 1918:
		if checkJulianLeap(year):
			return ("12.09." + str(year))
		else:
			return ("13.09." + str(year))

	elif year>1918:
		if checkGeorgianLeap(year):
			return ("12.09." + str(year))
		else:
			return ("13.09." + str(year))


year = int(input())

result = solve(year)

print(result)