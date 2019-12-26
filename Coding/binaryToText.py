def binaryToText(bin_code):
	text = str()
	symbols = bin_code.replace(' ', '')
	for i in range(len(symbols) // 8):
		text += chr(int(symbols[i * 8: (i + 1) * 8], 2))
	return text


if __name__ == '__main__':
	inp = input('Enter code in binary: ')
	print(binaryToText(inp))