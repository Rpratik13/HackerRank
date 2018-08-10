def arrayChange(inputArray):
    change = 0;
    for i in range(len(inputArray) - 1):
        if inputArray[i] >= inputArray[i + 1]:
            change += inputArray[i] - inputArray[i + 1] + 1;
            inputArray[i + 1] += inputArray[i] - inputArray[i + 1] + 1;

    return change;


print(arrayChange([1, 1, 1]))
