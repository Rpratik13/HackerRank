def sockMerchant(n,ar):
	list1 = []
	sell = 0
	for i in range(len(ar)):
		count = 1
		if ar[i] in list1:
			continue
		for j in range(i+1,len(ar)):
			if ar[i]==ar[j]:
				count+=1
		
		if count > 1 and count%2==0:
			sell = sell + count/2
		elif count > 1 and count%2!=0:
			sell = sell + (count-1)/2

		list1.append(ar[i])

	return int(sell)

n = int(input())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)

print(result)