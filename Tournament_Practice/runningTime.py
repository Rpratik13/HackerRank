def insertionSort(array):
    count = 0
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            count += 1
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return count


if __name__ == '__main__':
    n = int(input())
    lst = [int(inp) for inp in input().split()]
    print(insertionSort(lst))