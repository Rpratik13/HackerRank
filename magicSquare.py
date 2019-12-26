magic_squares = [
	[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
	[[8, 3, 4], [1, 5, 9], [6, 7, 2]],
	[[4, 3, 8], [9, 5, 1], [2, 7, 6]],
	[[4, 9, 2], [3, 5, 7], [8, 1, 6]],
	[[2, 9, 4], [7, 5, 3], [6, 1, 8]],
	[[2, 7, 6], [9, 5, 1], [4, 3, 8]],
	[[6, 7, 2], [1, 5, 9], [8, 3, 4]],
	[[6, 1, 8], [7, 5, 3], [2, 9, 4]]]


def formingMagicSquare(square: list) -> int:
	min_diff = float('inf')
	for x in range(8):
		diff = 0
		for row in range(0,3):
			for col in range(0,3):
				diff += abs(magic_squares[k][row][col] - square[row][col])
		min_diff = min(diff, min_diff)
	return min_diff	


if __name__ == '__main__':
	square = []

	for i in range(3):
		square.append(list(map(int, input().rstrip().split())))

	result = formingMagicSquare(square)

	print(result)