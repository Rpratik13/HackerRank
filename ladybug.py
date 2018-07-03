def ladybug(s):
	spaces=0
	length = len(s)
	list1 = []
	for i in range(length):
		if s[i]=='_':
			spaces+=1

	for i in range(length-2):
		if (s[i]!=s[i+1]) and (s[i+1]!=s[i+2]) and spaces==0:
			return "NO"

	if (length - spaces)==0:
		return "YES"
	else:
		for i in range(length):
			if (ord(s[i]) in list1) or (s[i]=='_'):
				continue
			j=i+1
			count = 0
			while j < length:
				if s[i]==s[j]:
					count+=1
				j+=1

			if count==0:
				return "NO"
			else:
				list1.append(ord(s[i]))
	return "YES"



q = int(input())

for q_itr in range(q):
	n = int(input())
	s = input()
	result = ladybug(s)
	print(result)