def happyLadybugs(b):
	bugs_color = list()
	for i in b:
		if i != '_':
			bugs_color.append(i)

	if b.count('_') != 0:
		for color in bugs_color:
			if b.count(color) < 2:
				return 'NO'
		return 'YES'
	else:
		current = b[0]
		count = 1
		for i in b[1:] + '#':
			if i != current and count == 1:
				return 'NO'
			elif i == current:
				count += 1
			else:
				current = i
				count = 1
		return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()