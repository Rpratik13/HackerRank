def kaprekarNumbers(p, q):
    kaprekar = list()
    for i in range(p, q + 1):
        n = i ** 2
        d = len(str(n)) // 2
        if n == i:
            kaprekar.append(i)
            continue
        
        if len(str(n)) == 1:
            x = '0' + str(n)
            d = len(x) // 2
        else:
            x = str(n)
        if int(x[:d]) + int(x[d:]) == i:
            kaprekar.append(i)

    if len(kaprekar) == 0:
        print('INVALID RANGE')
    else:
        for i in kaprekar:
            print('{}'.format(i), end=" ")        


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)