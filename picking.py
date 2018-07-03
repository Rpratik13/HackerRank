def pickingNumbers(arr):
	arr.sort()
	sum1 = 0
	max1 = 0
	list1 = []
	for i in range(len(arr)):

		sum1 = 1
		if arr[i] in list1:
			continue
		j = i+1
		while j < len(arr):
			if abs(arr[i]-arr[j])<2:
				sum1+=1
			j+=1
		list1.append(arr[i])
		list1.append(arr[i]+1)
		if max1<sum1:
			max1=sum1
	return max1

n = int(input())

a = list(map(int, input().rstrip().split()))

result = pickingNumbers(a)	
print(result)