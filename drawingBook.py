def forward(p):
	if p%2==0:
		return (p)//2
	else:
		return (p-1)//2


def backward(n,p):
	if n%2!=0:
		if p%2!=0:
			return (n-p)//2
		else:
			return (n-p-1)//2
	else:
		if p%2!=0:
			return ((n-p)//2)+1
		else:
			return (n-p)//2

def pageCount(n, p):
	a = forward(p)
	b = backward(n,p)
	if a<b:
		return a
	else:
		return b

n = int(input())

p = int(input())

result = pageCount(n, p)

print(result)