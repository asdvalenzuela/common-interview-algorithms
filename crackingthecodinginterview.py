# solution for strings and arrays 1.1

def has_unique_chars(strng):
	char_list = []
	for char in strng:
		if char in char_list:
			return False
		char_list.append(char)
	return True

def faster_has_unique_chars(strng):
	char_dict = {}
	for char in strng:
		if char in char_dict:
			return False
		else:
			char_dict[char] = True
	return True

# solution for strings and arrays 1.2

def reverse(strng):
	reverse = ''
	for char in strng:
		reverse = char + reverse
	return reverse

# solution for strings and arrays 1.3

def is_perm(str1, str2):
	if len(str1) != len(str2):
		return False
	char_dict1 = {}
	char_dict2 = {}
	for char in str1:
		char_dict1[char] = char_dict1.get(char, 0) + 1
	for char in str2:
		if char not in char_dict1:
			return False
		char_dict2[char] = char_dict2.get(char, 0) + 1
	for key in char_dict1:
		if char_dict1[key] != char_dict2[key]:
			return False
	return True

# solution for strings and arrays 1.4

def replace_spaces(strng):
	new_str = ''
	for char in strng:
		if char == ' ':
			new_str += '%20'
		else:
			new_str += char
	return new_str

# solution for strings and arrays 1.5

def compress(strng):
	# str.lower if necessary
	char_dict = {}
	for char in strng:
		char_dict[char] = char_dict.get(char, 0) + 1
	compressed = ''
	# the following two lines if answer needs to be alphabetical
	key_list = char_dict.keys()
	key_list.sort()
	for key in key_list:
		compressed += key
		compressed += str(char_dict[key])
	if len(compressed) > len(strng):
		return strng
	else:
		return compressed

# solution for linked lists 2.1

def remove_dupes(ll):
	node = self.head
	node_dict = {}
	node_dict[node.value] = True
	while node.next:
		if node.next.value in node_dict:
			node.next = node.next.next
		else:
			node_dict[node.next.value] = True
			node = node.next

# solution for linked lists 2.5

def add(ll1, ll2):
	node1 = ll1.head
	node2 = ll2.head
	sum_ll = LinkedList()
	carry = 0
	while node:
		sum_of = node1.value + node2.value + carry
		if sum_of > 9:
			tens, ones = str(sum_of)[0] + str(sum_of)[1]
			sum_ll.append_node(int(ones))
			carry = int(tens)
		else:
			sum_ll.append_node(sum)
		node1 = node.next
		node2 = node.next

# solution for trees 4.1

def is_balanced(root):
	depths = []
	nodes = [];
	nodes.append((root, 0))

	#while there are still nodes to check
	while len(nodes) != 0:
		node, depth = nodes.pop() 
		#end leaf case
		if not node.right and not node.left:
			#only need to append if depth is different than the ones we already have
			if depth not in depths:
				depths.append(depth)
			#if there are more than two distinct depths or if the difference is greater than 1, 
			#it is not a balanced tree
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

# solution for trees 4.5

def is_bst(root, lower_bound=None, upper_bound=None):
	if not root:
		return True
	if lower_bound is None and upper_bound is None:
		lower_bound = root.value
		upper_bound = root.value
	if root.value > upper_bound or root.value < lower_bound:
		return False
	return is_bst(root.left, lower_bound, root.value) and is_bst(root.right, root.value, upper_bound)

# iterative monkey chair problem

def chair_problem():
	chairs = range(1,101)
	skip = False
	i = 0
	while chairs.count('gone') < 99:
		while skip == False:
			if chairs[i%100] != 'gone':
				skip = True
			i += 1
		while skip == True:
			if chairs[i%100] != 'gone':
				chairs[i%100] = 'gone'
				skip = False
			i += 1
	return chairs

print chair_problem()
