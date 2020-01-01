def almostSorted(arr):
	misplaced = []
	sorted_arr = sorted(arr)
	for i in range(len(arr) - 1):
		if len(misplaced) == 0:
			if arr[i] > arr[i + 1]:
				misplaced.append(i)
		elif len(misplaced) == 1:
			if arr[i + 1] < arr[i]:
				misplaced.append(i + 1)
		if len(misplaced) == 1:
			arr[misplaced[0]], arr[misplaced[0] + 1] = arr[misplaced[0] + 1], arr[misplaced[0]]
			if arr == sorted_arr:
				return "yes \nswap {} {}".format(misplaced[0] + 1, misplaced[0] + 2)
			else:
				arr[misplaced[0]], arr[misplaced[0] + 1] = arr[misplaced[0] + 1], arr[misplaced[0]]
				
		elif len(misplaced) == 2:
			arr[misplaced[0]], arr[misplaced[1]] = arr[misplaced[1]], arr[misplaced[0]]
			if arr == sorted_arr:
				return "yes \nswap {} {}".format(misplaced[0] + 1, misplaced[1] + 1)
			else:
				arr[misplaced[0]], arr[misplaced[1]] = arr[misplaced[1]], arr[misplaced[0]]
			break
	rev = []
	for i in range(len(arr)):
		if len(rev) == 2:
			arr[rev[0]: rev[1] + 1] = arr[rev[0]: rev[1] + 1][::-1]
			if arr == sorted_arr:
				return 'yes \nreverse {} {}'.format(rev[0] + 1, rev[1] + 1)
			break
		if len(rev) == 0:
			if arr[i] > arr[i + 1]:
				rev.append(i)
		elif len(rev) == 1:
			if arr[i] < arr[i + 1]:
				rev.append(i)

	return "no"


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(almostSorted(arr))