def beautifulTriplets(n,d,val):
	count = 0;
	trip = [];
	for i in range(0,len(val)):
		for j in range(i+1,len(val)):
			if (i+j<len(val)):
				if (val[j] - val[i]==val[2*j-i]-val[j]):
					count+=1;
					trip.append([val[i],val[j],val[2*j-i]]);
					break;

	return count;






inp = [int(x) for x in input().split()];
n = inp[0];
d = inp[1];
val = [int(x) for x in input().split()];

result = beautifulTriplets(n,d,val);

print(result);