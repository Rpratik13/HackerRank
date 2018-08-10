def BonAppetit(k, bill, b):
    sum1 = 0
    for i in range(len(bill)):
        if i != k:
            sum1 += bill[i]

    sum1 = sum1 / 2
    if b == sum1:
        return "Bon Appetit"
    else:
        return int(b - sum1)


ar = list(map(int, input().rstrip().split()))

n = ar[0]

k = ar[1]

bill = list(map(int, input().rstrip().split()))

b = int(input())

result = BonAppetit(k, bill, b)

print(result)
