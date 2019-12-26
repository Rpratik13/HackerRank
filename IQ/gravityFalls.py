def gravityFalls(msg):
	code = str()
	for i in range(0, len(msg), 2):
		# print(int(msg[i:i+2]))
		code += chr(64 + int(msg[i:i + 2]))
	return code

if __name__ == '__main__':
	print(gravityFalls('1805220518190520080503091608051819'))