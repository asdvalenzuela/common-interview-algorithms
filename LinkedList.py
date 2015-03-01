class Node(object):

	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList(object):
	
	def __init__(self):
		self.head = None
		self.tail = None

	def append_node(self, value):
		node = Node(value)
		if self.head is None:
			self.head = node
		else:
			self.tail.next = node
		self.tail = node

	def print_ll(self):
		node = self.head
		while node:
			print node.value
			node = node.next

	def length(self):
		count = 0
		node = self.head
		while node:
			count += 1
			node = node.next
		return count

	def reverse(self):
		node = self.head
		next_node = node.next
		self.head.next = None
		while next_node:
			loop_node = next_node.next
			next_node.next = node
			node = next_node
			next_node = loop_node
		self.head = node

	def remove_dups(self):
		node = self.head
		ll_values = {}
		while node:
			ll_values[node.value] = True
			if node.next.value in ll_values:
				node.next = node.next.next
			node = node.next 

	def find_nth_node_from_end(self, n):
		index = 0
		node = self.head
		while node and index < n:
			node = node.next 
			index += 1	
		nth_node = self.head
		while node:
			node = node.next
			nth_node = nth_node.next
		return nth_node.value

	def find_nth_node_fromend(self,n):
		length = self.length()
		index = length - n
		count = 0
		node = self.head
		while node.next and count < index:
			node = node.next
			count += 1
		return node.value

	def add_node_by_index(self, data, index):
		new_node = Node(data)
		if index == 0:
			new_node.next = self.head
			self.head = new_node
		if index > self.len_list():
			return "index not in list"
		else:
			node = self.head
			count = -1
			while count < index-2:
				count += 1
				node = node.next
			new_node.next = node.next
			node.next = new_node

	def find_node_by_value(self, value):
		node = self.head
		index = -1
		while node:
			index += 1
			if node.data == value:
				return index
			node = node.next
		return None

	def find_node_by_index(self, index):
		if index == 0:
			return self.head.data
		if index > self.len_list():
			return "index not in list"			
		else:
			node = self.head
			count = 0
			while count < index:
				node = node.next
				count += 1
			return node.data

	def delete_node_by_value(self, value):
		if self.head.data == value:
			self.head = self.head.next
		else:
			node = self.head
			index = -1
			while node.next:
				index += 1
				if node.next.data == value:
					node.next = node.next.next
					return index + 1
				node = node.next
			return None

	def delete_node_by_index(self, index):
		if index == 0:
			self.head = self.head.next
		elif index > self.len_list():
			return "index not in list"
		else:
			node = self.head
			count = 0
			while count < index-1:
				node = node.next
				count += 1
			node.next = node.next.next

#monkey chair problem
def solve_chair_problem():
    chairs = LinkedList()
    for number in range(1,101):
        chairs.append_node(number)
    chairs.tail.next = chairs.head
    node = chairs.tail
    while node != node.next:
        next_node = node.next
        node.next = node.next.next
        node = next_node
    return node.data

#cracking the coding interview 2.5
def add(ll1, ll2):
	node1 = ll1.head
	node2 = ll2.head
	sum_ll = LinkedList()
	carry = 0
	while node1 and node2:
		sum_of = node1.data + node2.data + carry
		if sum_of > 9:
			tens, ones = str(sum_of)[0] + str(sum_of)[1]
			sum_ll.append_node(int(ones))
			carry = int(tens)
		else:
			sum_ll.append_node(sum_of)
		node1 = node1.next
		node2 = node2.next
	return sum_ll

#cracking the coding interview 2.5
def add_reverse(ll1, ll2):
	node1 = ll1.hea
	node2 = ll2.head
	sum_ll = LinkedList()
	carry = 0
	while node1 and node2:
		if node1.next and node2.next:
			sum_of = node1.next.data + node2.next.data
			if sum_of > 9:
				tens, ones = str(sum_of)[0] + str(sum_of)[1]
				carry = int(tens)
				sum_node = node1.data + node2.data + carry
				if sum_node > 9:
					tens, ones = str(sum_node)[0] + str(sum_node)[1]
					sum_ll.append_node(int(ones))
				else:
					sum_ll.append_node(node1.data + node2.data + carry)
			else:			
				sum_ll.append_node(node1.data + node2.data)
		else:
			sum_node = node1.data + node2.data
			if sum_node > 9:
					tens, ones = str(sum_node)[0] + str(sum_node)[1]
					sum_ll.append_node(int(ones))
		node1 = node1.next
		node2 = node2.next
	return sum_ll