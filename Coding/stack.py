class Stack:
	def __init__(self):
		self.stack = list()


	def push(self, value):
		self.stack.append(value)


	def pop(self):
		val = self.stack[-1]
		del self.stack[-1]
		return val


	def size(self):
		return len(self.stack)


	def isEmpty(self):
		return self.size == 0


	def top(self):
		return self.stack[-1]



if __name__ =='__main__':
	x = Stack()
	array = [5, 4, 3, 2, 1]
	for elem in array:
		x.push(elem)

	print(x.size())
	print(x.top())
	y = x.pop()
	print(x.size())