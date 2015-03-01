class Node(object):

	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


class BinarySearchTree(object):

	def __init__(self):
		self.root = None

	def append_node(self, value):
		new_node = Node(value)
		if not self.root:
			self.root = new_node
		else:
			node = self.root
			while value != node.value:
				if (value < node.value) and node.left:
					node = node.left
				elif value < node.value:
					node.left = new_node
				if (value > node.value) and node.right:
					node = node.right
				elif value > node.value:
					node.right = new_node

	def search_tree(self, value, node=None):
		if not node:
			node = self.root
		if value > node.value:
			if not node.right:
				return False
			return self.search_tree(value, node.right)
		if value < node.value:
			if not node.left:
				return False
			return self.search_tree(value, node.left)
		else:
			return True

	def df_traversal(self, node):
		if node:
			self.df_traversal(node.left)
			print node.value
			self.df_traversal(node.right)

	def bf_traversal(self):
		queue = [self.root]
		while queue:
			node = queue.pop(0)
			print node.value
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right) 

	def find_largest(node):
		while node:	
			if not node.right:
				return node.value
			node = node.right

	def find_2nd_largest_value(self):
		node = self.root

		while node: 
			#in this case, we need to find the largest node of the left subtree
			if node.left and not node.right:
				return self.find_largest(node.left)
			#in this case, node is the 2nd largest value as its right child has no ancestors
			if node.right:
				if not node.right.left and not node.right.right:
					return node.value
			#otherwise we continue right to find the greatest value
			node = node.right

	def is_bst(self, node, lower_bound=None, upper_bound=None):
		if not node:
			return True
		if not lower_bound and not upper_bound:
			lower_bound = node.value
			upper_bound = node.value
		if node.value > upper_bound or node.value < lower_bound:
			return False
		return self.is_bst(node.left, lower_bound, node.value) and self.is_bst(node.right, node.value, upper_bound)

	def is_balanced(self):
		depths = []
		nodes = [(self.root, 0)];

		while len(nodes) != 0:
			node, depth = nodes.pop() 

			#end leaf case
			if not node.right and not node.left:
				#only need to append if depth is different than the ones we already have
				if depth not in depths:
					depths.append(depth)
				#if there are more than two distinct depths or if the difference of two distinct depths
				# is greater than 1, it is not a balanced tree
				if (len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
					return False
			#if not end leaf, continue, incrementing depth as we go
			else:	
				if node.right:
					nodes.push(node.right, depth+1)
				if node.left:
					nodes.push(node.left, depth+1)
		#if there are no nodes left then the tree is balanced
		return True

	def serialize(self, node=None):
		f = open('serialize.txt', 'w')
		if not node:
			node = self.root
		if node:
			s = str(node.value) + '\n'
			f.write(s)	
			self.serialize(node.left)
			self.serialize(node.right)

def deserialize():
	tree = BinarySearchTree()
	f = open('serialize.txt', 'r')
	for line in f:
		line.strip()
		value = int(line)
		tree.append_node(value)
