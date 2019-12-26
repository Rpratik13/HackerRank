class Node:
	def __init__(self, value):
		self.value = value
		self.parent = None
		self.left = None
		self.right = None


class BST:
	def __init__(self):
		self.root = None


	def insert(self, value):
		if self.root == None:
			self.root = Node(value)
		else:
			return self._insert(self.root, value)

	def _insert(self, currentNode, value):
		if value < currentNode.value:
			if currentNode.left == None:
				currentNode.left = Node(value)
				currentNode.left.parent = currentNode
			else:
				return self._insert(currentNode.left, value)
		elif value > currentNode.value:
			if currentNode.right == None:
				currentNode.right = Node(value)
				currentNode.right.parent = currentNode
			else:
				return self._insert(currentNode.right, value)
		else:
			print('{} is already in tree.'.format(value))


	def largestKey(self):
		if self.root != None:
			return self._largestKey(self.root)

	def _largestKey(self, currentNode):
		if currentNode.right == None:
			return currentNode.value
		else:
			return self._largestKey(currentNode.right)


	def smallestKey(self):
		if self.root != None:
			return self._smallestKey(self.root)

	def _smallestKey(self, currentNode):
		if currentNode.left == None:
			return currentNode.value
		else:
			return self._smallestKey(currentNode.left)

	def traverse(self, mode='pre'):
		if mode == 'pre':
			print('Pre-order Traversal')
			return self._preorder(self.root)
		elif mode == 'in':
			print('In-order Traversal')
			return self._inorder(self.root)
		else:
			print('Post-order Traversal')
			return self._postorder(self.root)


	def _preorder(currentNode):
		if currentNode != None:
			print(currentNode.value)
			self._preorder(currentNode.left)
			self._preorder(currentNode.right)

	def _inorder(currentNode):
		if currentNode != None:
			self._preorder(currentNode.left)
			print(currentNode.value)
			self._preorder(currentNode.right)

	def _postorder(currentNode):
		if currentNode != None:
			self._preorder(currentNode.left)
			self._preorder(currentNode.right)
			print(currentNode.value)
