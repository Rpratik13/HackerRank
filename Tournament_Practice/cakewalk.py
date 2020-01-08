def cakewalk(calories):
	ans = 0
	pw = 0
	for i in calories:
		ans += i * (2 ** pw)
		pw += 1
	return ans


if __name__ == '__main__':
	n = int(input())
	calories = [int(inp) for inp in input().split()]
	print(cakewalk(sorted(calories, reverse = True)))