def migratoryBirds(ar):
	list1=[]
	id1=0
	max1=0
	for i in range(len(ar)):
		count = 1
		if ar[i] in list1:
			continue
		for j in range(i+1,len(ar)):
			if ar[i]==ar[j]:
				count+=1
		if max1<count:
			max1=count
			common = ar[i]
		elif max1==count and ar[i]<common:
			common = ar[i]
		list1.append(ar[i])
	return common

ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

result = migratoryBirds(ar)

print(result)