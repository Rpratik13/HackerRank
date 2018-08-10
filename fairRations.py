def fairRations(b):
	count = 0;
	last_changed = -1;
	for i in range(0,len(b)-1):
		if b[i]%2!=0:
			b[i]+=1;
			b[i+1]+=1;
			count+=2
			last_changed = i+1;
	if last_changed==-1 or b[last_changed]%2==0:
		return count;
	elif b[last_changed]%2!=0:
		return "NO";



n = int(input());
bread = [int(x) for x in input().split()];

result = fairRations(bread);
print(result);