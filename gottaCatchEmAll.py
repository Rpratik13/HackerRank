def gottaCatchEmAll(types, set_range):
	pokemons = types[set_range[0] - 1: set_range[1]]
	print(pokemons)
	pokemon_set = set(pokemons)
	for pokemon in pokemon_set:
		if pokemons.count(pokemon) > len(pokemons) // 2:
			return pokemon
	return 'Champion'


if __name__ == "__main__":
	nt = [int(inp) for inp in input().split()]
	n = nt[0]
	t = nt[1]
	types = [int(inp) for inp in input().split()]
	s = int(input())
	for x in range(s):
		set_range = [int(inp) for inp in input().split()]

		print(gottaCatchEmAll(types, set_range))
