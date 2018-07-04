def timeConversion(s):
	if s[8]=='P':
		if ord(s[0])==49 and ord(s[1])==50:
			x ="12" 	
		else:
			x = chr(ord(s[0]) + 1) + chr(ord(s[1]) + 2)
		ans = x 
		for i in range(2,len(s)-2):

			ans = ans + s[i]
		return ans
	elif s[8]=='A':
		if ord(s[0])==49 and ord(s[1])==50:
			x ="00" 	
			ans = x	+ s[2:8]
		else:
			ans = s[:8]
		return ans
	

s = input()

result = timeConversion(s)

print(result)