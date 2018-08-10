def circularArrayRotation(a, k,queries):
    ans = []
    n = k % len(a)
    x = a[:n] + a[n:] 

    for i in queries:
        ans.append(x[i])

    return ans





nkq = input().split()

n = int(nkq[0])

k = int(nkq[1])

q = int(nkq[2])

a = list(map(int, input().rstrip().split()))

queries = []

for n in range(q):
    queries_item = int(input())
    queries.append(queries_item)

result = circularArrayRotation(a, (k%len(a)), queries)
for i in result:
    print(i)