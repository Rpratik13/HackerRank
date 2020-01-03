def mock(s):
	upper = False
	ans = ''
	for i in s:
		if i.isalpha():
			if upper:
				ans += i.upper()
			else:
				ans += i.lower()
			
		else:
			ans += i
		upper = not upper
	return ans 

if __name__ == '__main__':
	print(mock(input()))