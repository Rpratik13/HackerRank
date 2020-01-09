  # Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = [int(inp) for inp in input().split()]
w = [int(inp) for inp in input().split()]

ans = 0
for i in range(n):
    ans += x[i] * w[i]
print(ans / sum(w))
