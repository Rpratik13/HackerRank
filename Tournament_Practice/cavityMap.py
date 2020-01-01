def sideNotX(i, j, matrix):
	if matrix[i - 1][j] != 'X' and matrix[i + 1][j] != 'X' and matrix[i][j - 1] != 'X' and matrix[i][j + 1] != 'X':
		return True
	return False

def cavityMap(n, matrix):
	for i in range(1, n - 1):
		for j in range(1, n - 1):
			if sideNotX(i, j, matrix) and int(matrix[i - 1][j]) < int(matrix[i][j]) and int(matrix[i + 1][j]) < int(matrix[i][j]) and int(matrix[i][j - 1]) < int(matrix[i][j]) and int(matrix[i][j + 1]) < int(matrix[i][j]):
				matrix[i][j] = 'X'

	ans = ''
	for i in range(n):
		ans += ''.join(matrix[i])
		ans += '\n'
	return ans


if __name__ == '__main__':
	n = int(input())
	matrix = list()
	for i in range(n):
		matrix.append([x for x in input()])
	print(cavityMap(n, matrix))