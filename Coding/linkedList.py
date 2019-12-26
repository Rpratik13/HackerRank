class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.root = None
		self.length = 0

	
	def insert(self, value):
		self.length += 1
		if self.root == None:
			self.root = Node(value)
		else:
			return self._insert(self.root, value)


	def _insert(self, currentNode, value):
		if currentNode.next == None:
			currentNode.next = Node(value)
		else:
			return self._insert(currentNode.next, value)

	
	def insertAfter(self, afterValue, value):
		if self.root != None:
			return self._insertAfter(self.root, afterValue, value)


	def _insertAfter(self, currentNode, afterValue, value):
		if currentNode.value == afterValue:
			temp = Node(value)
			if currentNode.next != None:
				temp.next = currentNode.next
				currentNode.next = temp
			else:
				currentNode.next = temp
		else:
			if currentNode.next != None:
				return self._insertAfter(currentNode.next, afterValue, value)
			else:
				print('{} not in list.'.format(afterValue))



	def delete(self, value):
		if self.root != None:
			if self.root.value == value:
				self.root = self.root.next
			else:
				return self._delete(self.root, value)


	def _delete(self, currentNode, value):
		if currentNode.next == None:
			print('{} not in list.'.format(value))
		elif currentNode.next.value == value:
			if currentNode.next.next != None:
				currentNode.next = currentNode.next.next
			else:
				currentNode.next = None
		else:
			return self._delete(currentNode.next, value)


	def search(self, value):
		position = 0
		if self.root != None:
			return self._search(self.root, position, value)


	def _search(self, currentNode, position, value):
		if currentNode.value == value:
			print(position)
		elif currentNode.next != None:
			return self._search(currentNode.next, position + 1, value)
		else:
			print(-1)


	def traverse(self):
		if self.root != None:
			return self._traverse(self.root)


	def _traverse(self, currentNode):
		print(currentNode.value)
		if currentNode.next != None:
			return self._traverse(currentNode.next)


if __name__ == '__main__':
	ll = LinkedList()
	array = [5, 4, 2, 10, 2, 6, 4, 1]
	for i in array:
		ll.insert(i)

	ll.insertAfter(10, 9)
	ll.insertAfter(9, 100)
	# ll.delete(5)
	# ll.search(1)	
	ll.traverse()
	# print(ll.search(10))
