def sqroot(n):
	num = n;
	position = 1;
	ans = 0;
	while (position!=10 and ans*ans!=num):
		length = len(str(n));

		if (length-2)>0:
			if(length%2)==0:
				div = length - 2;
				temp = n // (10**div);
			else:
				div = length - 1;
				temp = n //(10**div);
		elif (length-2)==0:
			temp = n;
		elif(length-2==-1):
			temp = n*100
			mark = position;
		
		
		ap = 0;
		while((ans*2*10+(ap+1))*(ap+1))<=temp:
			ap +=1;
		ans = ans *10 + ap;
		position+=1
		n = ((temp-(ap*ap))*(10**div))+n%(10**div);
	return ans


inp = int(input());
result = sqroot(inp);
print(result);