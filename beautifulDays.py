def reverse(n):
	t = n
	reverse = 0
	while t != 0:
		rem = t % 10
		reverse = reverse * 10 + rem
		t = t//10
	return reverse 

def beautifulDays(i, j, k):
	count=0
	for n in range(i,j+1):
		if (abs(n-reverse(n))%k)==0:
			count+=1
	return count




ijk = input().split()

i = int(ijk[0])

j = int(ijk[1])

k = int(ijk[2])

result = beautifulDays(i, j, k)

print(result)