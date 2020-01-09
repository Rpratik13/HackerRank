def partition(array):
    p = array[0]
    less = []
    grt = []

    for i in range(1, len(array)):
        if array[i] < p:
            less.append(array[i])
        else:
            grt.append(array[i])

    ans = less + [p] + grt

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    n = int(input())
    lst = [int(inp) for inp in input().split()]
    print(partition(lst))