def checkGeorgianLeap(year):
	if year%400==0:
		return True
	elif year%100==0: 
		return False
	elif year%4==0:
		return True


year = int(input())

print(checkGeorgianLeap(year))