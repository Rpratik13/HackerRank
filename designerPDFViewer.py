def designerPdfViewer(h,word):
	list1 = []
	for i in (range(len(word))):
		index = ord(word[i])-97
		list1.append(h[index])

	size = max(list1)*len(word)

	return size


h = list(map(int, input().rstrip().split()))

word = input()

result = designerPdfViewer(h, word)

print(result)