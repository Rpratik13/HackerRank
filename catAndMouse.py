def catAndMouse(x, y, z):
    catA = abs(x-z)
    catB = abs(y-z)
    if catA<catB:
        return "Cat A"
    elif catA>catB:
        return "Cat B"
    elif catA==catB:
        return "Mouse C" 

q = int(input())

for q_itr in range(q):
    xyz = input().split()

    x = int(xyz[0])

    y = int(xyz[1])

    z = int(xyz[2])

    result = catAndMouse(x, y, z)

    print(result)