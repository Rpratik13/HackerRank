# Enter your code here. Read input from STDIN. Print output to STDOUT
def median(num):
    if len(num) % 2 == 0:
        return (num[(len(num) - 1) // 2] + num[(len(num)) // 2]) // 2
    else:
        return num[(len(num)) // 2]


n = int(input())
num = [int(i) for i in input().split()]
num.sort()
q2 = median(num)
l = [i for i in num if i < q2]
r = [i for i in num if i > q2]
print(num)
print(l)
print(r)
q1 = median(l)
q3 = median(r)
print(q1)
print(q2)
print(q3)
