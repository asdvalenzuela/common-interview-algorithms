import random

#QUESTION 42
def merge_arrays(arr1, arr2):
	merged = []
	while len(arr1) != 0 and len(arr2) != 0:
		if arr1[0] < arr2[0]:
			merged.append(arr1.pop(0))
		else:
			merged.append(arr2.pop(0))
	merged = merged + arr1 + arr2
	return merged

# my_array     = [3,4,6,10,11,15]
# alices_array = [1,5,8,12,14,19]

# print merge_arrays(my_array, alices_array)
# prints [1,3,4,5,6,8,10,11,12,14,15,19]

#QUESTION 37
def rand7():
	return random.choice([1,2,3,4,5,6,7])
def rand5():
	while True:
		val = rand7()
		if val > 5:
			continue
		else:
			return val

# print rand5()

#QUESTION 36
def is_riffled_once(shuffled_deck, half1, half2):
	for card in shuffled_deck:
		if len(half1) != 0 and card == half1[0]:
			half1.pop(0)
		elif len(half2) != 0 and card == half2[0]:
			half2.pop(0)
		else:
			return False
	return True

#QUESTION 35
def get_random(floor, ceiling):
	return random.choice(range(floor, ceiling+1))

def shuffle(arr):
	if len(arr) <= 1:
		return arr
	for index in range(len(arr)):
		swap_index = get_random(index, len(arr)-1)
		arr[index], arr[swap_index] = arr[swap_index], arr[index]
	return arr

# arr = [1,2,3,4,5]

# print shuffle(arr)
# print shuffle(arr)

#QUESTION 34
def count_words(string):
	punctuation = {',': True, '.': True, ':': True, ' ': True, '!': True, '?': True, ';': True, '-': True}
	word_to_count = {}
	first_index = 0
	for index in range(len(string)):
		if string[index] in punctuation:
			word = string[first_index:index].lower()
			if word == '':
				continue
			word_to_count[word] = word_to_count.get(word, 0) + 1
			first_index = index + 1
	return word_to_count

# string = 'After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar.'

# print count_words(string)

#QUESTION 33
def find_duplicate(arr):
	existing_numbers = {}
	for number in arr:
		if number in existing_numbers:
			return number
		else:
			existing_numbers[number] = True
	return None

# arr = [0,1,2,3,1,4]
# print find_duplicate(arr)

#QUESTION 32
def sort_scores(unsorted_scores, highest_possible_score):
	scores_to_count = {}
	sorted_scores = []
	for score in unsorted_scores:
		scores_to_count[score] = scores_to_count.get(score, 0) + 1
	for score in scores_to_count:
		for number in range(scores_to_count[score]):
			sorted_scores.append(score)
	return sorted_scores

#QUESTION 31
def generate_perms(string):
	if len(string) <= 1:
		return [string]

	all_chars_except_last = string[:-1]
	last_char = string[-1]

	perms_of_all_chars_except_last = generate_perms(all_chars_except_last)
	permutations = []
	for perm in perms_of_all_chars_except_last:
		for position in range(len(all_chars_except_last)+1):
			permutation = perm[:position] + last_char + perm[position:]
			permutations.append(permutation)
	return permutations

#QUESTION 30
def is_permutation(string):
	char_to_count = {}
	for char in string:
		char_to_count[char] = char_to_count.get(char, 0) + 1
	odd_count = 0
	for key, value in char_to_count.iteritems():
		if value % 2 != 0:
			odd_count += 1
	if odd_count <= 1:
		return True
	return False

# print is_permutation('civic')
# print is_permutation('civil')

#QUESTION 29
def is_closed(string):
	openers_to_closers = {'{': '}', '[': ']', '(': ')'}
	closers = openers_to_closers.values()
	openers = []
	for char in string:
		if char in openers_to_closers:
			openers.append(char)
		elif char in closers:
			if char == openers_to_closers[openers[-1]]:
				openers.pop()
			else:
				return False
	return True

# print is_closed('{ [ ] ( ) }')
# print is_closed('{ [ ( ] ) }')
# print is_closed('{ [ }')

#QUESTION 28
def find_closing_paren_index(string, position):
	open_parens = []
	for index in range(position, len(string)):
		if string[index] == '(':
			open_parens.append('(')
		if string[index] == ')':
			open_parens.pop()
			if len(open_parens) == 0:
				return index

# string = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
# print find_closing_paren_index(string, 10)

#QUESTION 27
def reverse_words(string):
	words = string.split(' ')
	for index in range(len(words)/2):
		words[index], words[-(index + 1)] = words[-(index+1)], words[index]
	return (' ').join(words)

# message = 'find you will pain only go you recordings security the into if'
# print reverse_words(message)

#QUESTION 25
def kth_to_last_node(k, head_node):
	node = head_node
	count = 0
	while node and count < k:
		node = node.next
		count += 1
	kth_to_last_node = head_node
	while node:
		node = node.next
		kth_to_last_node = kth_to_last_node.next
	return kth_to_last_node.value

#QUESTION 24
def reverse(head_node):
	node = head_node
	next_node = node.next
	head_node.next = None
	while next_node:
		loop_node = next_node.next
		next_node.next = node
		node = next_node
		next_node = loop_node
	head_node = node
	return head_node

#QUESTION 23
def contains_cycle(head_node):
	slow = head_node
	fast = head_node
	while fast != None and fast.next != None:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			return True
	return False

#QUESTION 19
instack = []
outstack = []
def enqueue(value):
	instack.append(value)

def dequeue():
	if len(outstack) == 0:
		while len(instack) != 0:
			outstack.append(instack.pop())
	return outstack.pop()

#QUESTION 20
class MaxStack:

	def __init__(self):
		self.stack = Stack()
		self.maxs_stack = Stack()

	def push(self, item):
		self.stack.push(item)
		if item >= self.maxs_stack.peek():
			self.maxs_stack.push(item)

	def pop(self):
		item = self.stack.pop()
		if item == self.maxs_stack.peek():
			self.maxs_stack.pop()
		return item

	def get_max(self):
		return self.maxs_stack.peek()

#QUESTION 9
def is_bst(root, lower_bound=None, upper_bound=None):
	if not root:
		return True
	if lower_bound is None and upper_bound is None:
		lower_bound = root.value
		upper_bound = root.value
	if root.value > upper_bound or root.value < lower_bound:
		return False
	return is_bst(root.left, lower_bound, root.value) and is_bst(root.right, root.value, upper_bound)

#QUESTION 8
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

#QUESTION 10
def find_largest(root):
	node = root
	while node:	
		if not node.right:
			return node.value
		node = node.right

def find_2nd_largest_value(root):
	node = root

	while node: 
		#in this case, we need to find the largest node of the left subtree
		if node.left and not node.right:
			return find_largest(node.left)
		#in this case, node is the 2nd largest value as its right child has no ancestors
		if node.right:
			if not node.right.left and not node.right.right:
				return node.value
		#otherwise we continue right to find the greatest value
		node = node.right

#QUESTION 1
#keep track of min and max to the right
def find_best_profit(stock_prices_yesterday):
	min_price = stock_prices_yesterday[0]
	max_profit = 0
	for current_price in stock_prices_yesterday:
		min_price = min(min_price, current_price)
		max_profit = max(max_profit, current_price - min_price)
	return max_profit

# stock_prices_yesterday = [500, 300, 200, 100, 400, 800]
# print find_best_profit(stock_prices_yesterday)

def find_largest_difference(lst):
	min_val = lst[0]
	max_val = lst[0]
	for val in lst:
		min_val = min(min_val, val)
		max_val = max(max_val, val)
	return max_val-min_val

# print find_largest_difference([5,4,3,2,1])
# print find_largest_difference([1,2,3,4,5])

#QUESTION 2
def product_of_other_nums(lst):
	products = []
	for index in range(len(lst)):
		product = 1
		for other_index in range(len(lst)):
			if other_index != index:
				product *= lst[other_index]
		products.append(product)
	return products

# print product_of_other_nums([1,7,3,4])

#iterative solution to fibonnaci
def find_nth_fibonnaci(n):
	if n == 0 or n == 1:
		return n
	first_num = 0
	second_num = 1
	index = 3
	while index <= n:
		nth_num = first_num + second_num
		first_num, second_num = second_num, nth_num
		index += 1
	return nth_num

# print find_nth_fibonnaci(3)
# print find_nth_fibonnaci(8)
