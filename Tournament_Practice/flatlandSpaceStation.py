def flatlandSpaceStation(n, cities):
	cities.sort()
	ans = 0
	for city in range(len(cities) - 1):
		ans = max(ans, abs(cities[city] - cities[city + 1]) // 2)

	return max(ans, min(cities) - 0, (n - 1) - max(cities))

if __name__ == '__main__':
	nm = [int(inp) for inp in input().split()]
	cities = [int(inp) for inp in input().split()]

	print(flatlandSpaceStation(nm[0], cities))