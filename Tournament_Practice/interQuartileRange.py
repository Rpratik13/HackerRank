# Enter your code here. Read input from STDIN. Print output to STDOUT
def median(num):
    if len(num) % 2 == 0:
        return (num[(len(num) - 1) // 2] + num[(len(num)) // 2]) / 2
    else:
        return num[(len(num)) // 2]


n = int(input())
temp = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]

num = list()

for i, j in zip(temp, f):
	for x in range(j):
		num.append(i)
num.sort()



q2 = median(num)
if q2 in num:
	idx = (len(num)) // 2
	l = num[:idx]
	r = num[idx+1:]
else:
	l = [i for i in num if i < q2]
	r = [i for i in num if i > q2]

q1 = median(l)
q3 = median(r)

print('{:.1f}'.format(q3 - q1))