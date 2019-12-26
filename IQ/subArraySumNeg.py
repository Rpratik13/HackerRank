def subArraySumNeg(array, sum):
    current_sum = 0
    Map = {}
    for i in range(0, len(array)):
        current_sum += array[i]

        if (current_sum == sum):
            return 0, i

        if (current_sum - sum) in Map:
            return (Map[current_sum - sum] + 1), i

        Map[current_sum] = i


    return -1


if __name__ == '__main__':
    array = [10, -2, 2, 20, 10]
    sum = 20
    print(subArraySumNeg(array, sum))