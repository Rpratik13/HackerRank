def timeInWords(h,m):
	words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
	         "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six",
	         "twenty seven", "twenty eight", "twenty nine", "thirty"]

	if h > 12:
		h %= 12
	if (m == 0):
		return words[h - 1] + " o' clock"
	elif(m == 15):
		return "quarter past " + words[h - 1]
	elif(m == 30):
		return "half past " + words[h]
	elif(m == 45):
		return "quarter to " + words[h]
	elif(m == 1):
		return words[m - 1] + " minute past " + words[h - 1]
	elif(m > 1 and m < 30):
		return words[m - 1] + " minutes past " + words[h - 1]
	elif(m > 30 and m < 60):
		return words[59 - m] + " minutes to "+ words[h]


h = int(input());
m = int(input());

result = timeInWords(h,m);

print(result);