def cutTheSticks(arr):
	ans = []
	while max(arr)!=0:
		while min(arr)==0:
			arr.remove(0)
		min1 = min(arr)
		count = 0
		for i in range(0,len(arr)):
			arr[i]-=min1
			count+=1
		ans.append(count)
	return ans

n = int(input())

arr = list(map(int, input().rstrip().split()))

result = cutTheSticks(arr)

for i in result:
	print(i)