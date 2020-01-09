def partition(array: list) -> list:
    p = array[0]
    less = []
    grt = []

    for i in range(1, len(array)):
        if array[i] < p:
            less.append(array[i])
        else:
            grt.append(array[i])

    ans = quickSort(less) + [p] + quickSort(grt)
    print(' '.join(map(str, ans)))
    return ans

def quickSort(array: list) -> list:
    if len(array) > 1:
        return partition(array)
    return array



if __name__ == '__main__':
    n = int(input())
    lst = [int(inp) for inp in input().split()]
    quickSort(lst)