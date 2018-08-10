def appendAndDelete(s, t, k):
	i=0
	j=0
	count_s = count_t = 0
	while(s[i]==t[j] ):
		i+=1
		j+=1
		count_s+=1
		count_t+=1
		if i>=len(s) or j>=len(t):
			break
	
	cut = len(s)-count_s
	add = len(t)-count_t

	if (s==t):
		if(k>(2*len(s))):
			return "Yes"
		elif(k%2!=0):
			return "No"
		else:
			return "Yes"
	if (cut+add)==k:
		return "Yes"
	else:
		return "No"

s = input()

t = input()

k = int(input())

result = appendAndDelete(s, t, k)

print(result)