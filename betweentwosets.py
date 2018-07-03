def getTotalX(a,b):
	max1 = max(a)
	min1 = min(b)
	list1 = []
	list2 = []
	for i in range(max1,min1+1):
		count=0
		for j in a:
			if (i%j)==0:
				count+=1

		if count==len(a):
			list1.append(i)
	
	print (list1)

	for i in list1:
		count = 0
		for j in b:
			if j%i==0:
				count+=1
		if count==len(b):
			list2.append(j)

	return len(list2)

nm = input().split()

n = int(nm[0])

m = int(nm[1])

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

total = getTotalX(a, b)
print(total)