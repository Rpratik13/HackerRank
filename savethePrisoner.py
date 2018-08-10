def saveThePrisoner(n, m, s):
    x=s-1+m
    if (x%n)==0:
        return n
    else:
        return x%n



t = int(input())

for t_itr in range(t):
    nms = input().split()

    n = int(nms[0])

    m = int(nms[1])

    s = int(nms[2])

    result = saveThePrisoner(n, m , s)

    print(result)