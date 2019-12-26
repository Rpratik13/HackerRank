def fileNames(nameList):
	named = {}
	renamed = []
	for name in nameList:
		if name in named.keys():
			renamed.append(name + ' (' + str(named[name]) + ')')
			named[name + ' (' + str(named[name]) + ')'] = 1
			named[name] += 1
		else:
			renamed.append(name)
			named[name] = 1
	return renamed



if __name__ == '__main__':
	print(fileNames(['New Folder', 'New Folder', 'New Folder', 'New Folder (1)', 'New Folder (1)', 'New Folder (2)']))