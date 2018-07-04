def getMoneySpent(keyboards, drives, b):
        max1 = 0
        min1 = keyboards[0]+drives[0]
        for i in keyboards:
            for j in drives:
                if (i+j)>max1 and (i+j)<=b:
                    max1 = i+j
                if (i+j)<min1:
                    min1 = i+j

        if min1 > b:
            return -1
        
        return (max1)

bnm = input().split()

b = int(bnm[0])

n = int(bnm[1])

m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))

drives = list(map(int, input().rstrip().split()))

moneySpent = getMoneySpent(keyboards, drives, b)

print(moneySpent)