def lonelyInteger(lst,check_lst):
	for i in check_lst:
		if lst.count(i)==1:
			return i;


n = int(input());
lst = [int(x) for x in input().split()];
check_lst = list(set(lst));

print(lonelyInteger(lst,check_lst));