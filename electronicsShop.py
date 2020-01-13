def getMoneySpent(keyboards, drives, b):
        mx = 0
        mn = keyboards[0] + drives[0]
        for i in keyboards:
            for j in drives:
                if (i + j) <= b:
                    mx = max(mx, i + j)
                
                mn = min(mn, i + j)

        if mn > b:
            return -1
        
        return mx

bnm = input().split()

b = int(bnm[0])

n = int(bnm[1])

m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))

drives = list(map(int, input().rstrip().split()))

moneySpent = getMoneySpent(keyboards, drives, b)

print(moneySpent)