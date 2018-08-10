def selectionSort(arr):
    for fillSlot in range(len(arr) - 1, 0, -1):
        positionOfMax = 0
        for position in range(fillSlot + 1):
            if arr[position] > arr[positionOfMax]:
                positionOfMax = position

        arr[positionOfMax], arr[fillSlot] = arr[fillSlot], arr[positionOfMax]

    return arr


print(selectionSort([45, 2, 6, 3, 3, 7, 2, 47, 23, 4, 46, 74]))
