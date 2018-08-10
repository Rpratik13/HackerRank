def checkPalindrome(n):
    return (str(n) == str(n)[::-1]);


def convertBase(n, k):
    ans = 0
    pw = 0
    while(n != 0):
        val = n % k
        ans = ans + (10**pw) * val
        n = n // k
        pw += 1
    return ans


n = int(input("Range: "))
k = int(input("Base: "))

sm = 0
for i in range(11, n):
    if (checkPalindrome(i) and checkPalindrome(convertBase(i, k))):
        print(i, end=" ")
        print(convertBase(i, k))
        sm += i

print(sm)
