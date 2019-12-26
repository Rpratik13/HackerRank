def subArrayWithSum(array, sum):
	current_sum = array[0]
	start = 0
	for i in range(1, len(array)):
		while (current_sum > sum and start < i - 1):
			current_sum -= array[start]
			start += 1

		if (current_sum == sum):
			return start, (i - 1)
		current_sum += array[i]
	return -1


if __name__ == '__main__':
	sm = int(input('Enter Sum: '))
	array = [int(i) for i in input().split()]
	print(subArrayWithSum(array, sm))