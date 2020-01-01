def lisaWorkbook(k, arr):
	ans = 0
	page = 0
	for i in arr:
		chap_prob = []
		lst = []
		for x in range(1, i + 1):
			if len(lst) == k:
				chap_prob.append(lst)
				lst = []
				count = 0
			lst.append(x)
		if len(lst) != 0:
			chap_prob.append(lst)
		for j in chap_prob:
			page += 1
			if page in j:
				ans += 1
	return ans


if __name__ == '__main__':
	nk = [int(inp) for inp in input().split()]
	n = nk[0]
	k = nk[1]
	arr = [int(inp) for inp in input().split()]
	print(lisaWorkbook(k, arr))