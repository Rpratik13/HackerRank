def caesarCipher(s, k):
	y=""
	for i in range(len(s)):
		if s[i].isalpha():
			if s[i].isupper():
				if ord(s[i])+k>90:
					q = ord(s[i])+k-90
					x = chr(ord('A') + q-1) 
				else:
					x = chr(ord(s[i]) + k)	
			elif s[i].islower():
				if ord(s[i])+k>122:
					q = ord(s[i])+k-122
					x = chr(ord('a') + q-1) 
				else:
					x = chr(ord(s[i]) + k)	
			else:
				x = chr(ord(s[i]) + k)
			y = y + x
		else:
			y = y + s[i]	
	return y

n = int(input())

s = input()

k = int(input())
x=k%26
result = caesarCipher(s, x)
print(result)