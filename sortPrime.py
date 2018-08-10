from math import sqrt, ceil


def checkPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    for i in range(3, ceil(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def sortPrime(inp):
    inp.sort()
    for i in inp:
        if checkPrime(i):
            yield(i)


def main():
    inp = [int(x) for x in input().split()]
    result = sortPrime(inp)
    print("The entered prime numbers in ascending order are: ")
    for i in result:
        print(i)


if __name__ == '__main__':
    main()
