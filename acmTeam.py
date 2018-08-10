def acm(topic):
	result = []
	for i in range(0,len(topic)-1):
		count = 0;
		for j in range(0,len(topic)):
			if topic[i][j]=='1' or topic[i+1][j]=='1':
				count += 1;
		result.append(count);
	return result;


inp = input().split();

mem = inp[0];

top = inp[1];

topic = [];

for i in range(0,int(mem)):
	topic_items = input();
	topic.append(topic_items);


result = acm(topic)

for i in result: 	
	print(i)