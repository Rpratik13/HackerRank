def dividedDifference(x,y):
	length = len(y)
	h = 1

	diff = []
	diff2 = []
	check = True
	while check:
		i=0
		while(i+h<len(x) and i+1<len(y)):
			temp = (y[i+1]-y[i])/(x[i+h]-x[i])
			diff2.append(temp)
			i+=1
		diff.append(diff2[0])
		y = diff2
		diff2 = []
		h+=1
		if h == length:
			check = False
	return diff


x = [0,1,2,3]
y = [1,1,5,1]

inp = int(input("Enter required value: "))
difference = dividedDifference(x,y)


ans = 0
for i in range(0,len(y)-1):
	prod = 1
	for j in range(0,i+1):
		prod *= (inp-x[j])
	prod *= difference[i]
	ans += prod

ans += y[0]

print(ans)