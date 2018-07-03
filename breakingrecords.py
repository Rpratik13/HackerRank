def breakingRecords(scores):
	max1=min1=scores[0]
	max_break=min_break=0
	result = []
	for i in range(1,len(scores)):
		if scores[i]>max1:
			max1=scores[i]
			max_break+=1

		if scores[i]<min1:
			min1=scores[i]
			min_break+=1

	result.append(max_break)
	result.append(min_break)
	return result


n = int(input())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)

for i in result:
	print(i,end=" ")