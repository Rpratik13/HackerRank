def checkDivisible(i,num):
	for x in num:
		if(i%x!=0):
			return True;
	return False;


def lcm(num):
	i = max(num);
	while(checkDivisible(i,num)):
		i += max(num);
	return i;

num = [int(i) for i in input().split()	];
result = lcm(num);

print("The L.C.M. of ",end="");
for i in range(len(num)):
	print(num[i],end="");
	if (i==len(num)-2):
		print(" and ",end="");
	elif(i==len(num)-1):
		print("",end="")
	else:
		print(", ",end="");
print(" is",end=" ")
print(result);
