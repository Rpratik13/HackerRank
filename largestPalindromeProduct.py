def checkPalindrome(n):
	t = n
	result=0
	while t!=0:
		result = result *10 + t%10
		t = t//10
	if n == result:
		return True
	else:
		return False




def largestPalindromeProduct(n):
	r = 0
	for i in range(990,99,-11):
		for j in range(999,99,-1):
			t = i*j
			if (checkPalindrome(t) and r<t and t<n):
				r = t
				break
			elif(t<r):
				break
	return r


t = int(input())
for i in range(0,t):

	n = int(input())

	result = largestPalindromeProduct(n)

	print(result)
