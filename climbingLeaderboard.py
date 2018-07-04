def slicingScores(scores):
	list2 = []
	for i in range(len(scores)):
		if scores[i] in list2:
			continue
		else:
			list2.append(scores[i])
	return list2


def climbingLeaderboard(scores,alice):
	list1=[]
	for j in range(len(alice)-1,-1,-1):
		position = len(scores) + 1
		if alice[j]<=scores[len(scores)-1]:
			list1.append(position)

		elif (alice[j]>=scores[0]):	
			list1.append(1)

		else:
			for i in range(len(scores)-2,-1,-1):
				position-=1
				if alice[j]<scores[i]:
					list1.append(position)
					break
				elif alice[j]==scores[i]:
					list1.append(position-1)
					break
			
	return list1


scores_count = int(input())

scores = list(map(int, input().rstrip().split()))

alice_count = int(input())

alice = list(map(int, input().rstrip().split()))

result = climbingLeaderboard(slicingScores(scores), alice)

for i in range(len(result)-1,-1,-1):
	print(result[i])