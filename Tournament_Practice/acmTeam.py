def acm(topic):
	result = [0, 0]
	for i in range(len(topic) - 1):
		for j in range(i + 1,len(topic)):
			count = ('{:b}'.format((int(topic[i], 2) | int(topic[j], 2)))).count('1')
			if count == result[0]:
				result[1] += 1
			elif count > result[0]:
				result[0] = count;
				result[1] = 1
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