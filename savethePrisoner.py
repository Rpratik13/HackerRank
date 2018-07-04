def sum(n):
    if n<=1:
        return 1
    else:
        return sum(n-1)+n


def saveThePrisoner(n, m, s):
    m = sum(m//n)
    for i in range(1,m+1):
        s = s+1
        if s>n:
            s=1
    return s



t = int(input())

for t_itr in range(t):
    nms = input().split()

    n = int(nms[0])

    m = int(nms[1])

    s = int(nms[2])

    result = saveThePrisoner(n, m , s)

    print(result)