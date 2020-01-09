def printArray(array):
    for i in array:
        print(i, end = " ")
    print('')


def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            printArray(array)
        if array[j + 1] != key:
            array[j + 1] = key
            printArray(array)


if __name__ == '__main__':
    n = int(input())
    lst = [int(inp) for inp in input().split()]
    insertionSort(lst)