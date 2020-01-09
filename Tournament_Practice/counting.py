def countingSort(n, array):
	count = [0] * (n)
	
	for i in array:
		count[i] += 1


	print(' '.join(map(str, count[:100])))

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    countingSort(n, arr)

