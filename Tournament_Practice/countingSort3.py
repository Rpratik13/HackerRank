def countingSort(array):
	count = [0] * max(101, (max(array) + 1))
	sort = [None] * len(array)

	for i in array:
		count[i] += 1

	for i in range(1, len(count)):
		count[i] += count[i - 1]

	for i in array[::-1]:
		sort[count[i] - 1] = i
		count[i] -= 1
	
	for i in range(1, 101):
		print(count[i], end = ' ')


if __name__ == '__main__':

    n = int(input())
    arr = []
    for i in range(n):
    	inp = int(input().split(' ')[0])
    	arr.append(inp)
    countingSort(arr)

