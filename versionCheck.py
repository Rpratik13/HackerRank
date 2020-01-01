def versionCheck(version1, version2):
	if version1[0] > version2[0]:
		return True
	elif version1[0] < version2[0]:
		return False
	elif len(version1) > 1:
		return versionCheck(version1[1:], version2[1:])
	else:
		return 'Same'

if __name__ == '__main__':
	version1 = [int(i) for i in input('Enter version1: ').split('.')]
	version2 = [int(i) for i in input('Enter version2: ').split('.')]

	if versionCheck(version1, version2) == 'Same':
		print('Same Version')
	elif versionCheck(version1, version2):
		print('{} is newer than {}.'.format('.'.join([str(i) for i in version1]), '.'.join([str(i) for i in version2])))
	else:
		print('{} is newer than {}.'.format('.'.join([str(i) for i in version2]), '.'.join([str(i) for i in version1])))
