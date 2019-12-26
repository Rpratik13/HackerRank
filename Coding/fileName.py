def fileName(names: list) -> list:
	taken = dict()
	renamed = list()
	for name in names:
		if name not in taken:
			taken[name] = 1
			renamed.append(name)
		else:
			newName = name + ' (' + str(taken[name]) + ')'
			taken[newName] = 1
			taken[name] += 1
			renamed.append(newName)
	return renamed


if __name__ == '__main__':
	names = list(map(str, input().split()))
	print(fileName(names))