def countingValleys(n, s):
	start = 0
	valleys = 0
	for i in range(len(s)):
		if s[i] =='U':
			if start == 0:
				start = 1
			else:
				start +=1
		elif s[i]=='D':
			if start ==0:
				start = -1
				valleys +=1
			else:
				start-=1
	return valleys 

n = int(input())

s = input()

result = countingValleys(n, s)

print(result)