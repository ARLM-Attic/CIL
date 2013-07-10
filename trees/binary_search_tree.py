
# Binary search tree traversals and finding

class TreeNode():
	left = None
	right = None
	data = None
	
	def __init__(self, data):
		self.data = data
	

# Description: 		Pre-order traversal
# Improvements:		None
# Limitation:		Space usage for call stack
# Time complexity:	O(n)
# Space complexity:	O(n) (for list, O(log n) for call stack)
def pre_order(node):
	if node == None:	#Driver function for root, eliminates an if per call
		return []
	res = []
	pre_order_(node, res)
	return res

def pre_order_(node, res):
	res.append(node.data)
	if node.left != None:
		pre_order_(node.left, res)
	if node.right != None:
		pre_order_(node.right, res)



# Description: 		In-order traversal and print
# Improvements:		None
# Limitation:		Space usage for call stack
# Time complexity:	O(n)
# Space complexity:	O(n) (for list, O(log n) for call stack)
def in_order(node):
	if node == None:	#Driver function for root, eliminates an if per call
		return []
	res = []
	in_order_(node, res)
	return res

def in_order_(node, res):
	if node.left != None:
		in_order_(node.left, res)
	res.append(node.data)
	if node.right != None:
		in_order_(node.right, res)
		
		
# Description: 		Post-order traversal and print
# Improvements:		None
# Limitation:		Space usage for call stack
# Time complexity:	O(n)
# Space complexity:	O(n) (for list, O(log n) for call stack)
def post_order(node):
	if node == None:	#Driver function for root, eliminates an if per call
		return []
	res = []
	post_order_(node, res)
	return res

def post_order_(node, res):
	if node.left != None:
		post_order_(node.left, res)
	if node.right != None:
		post_order_(node.right, res)
	res.append(node.data)
	
	
# Description: 		Reverse-order traversal and print
# Improvements:		None
# Limitation:		Space usage for call stack
# Time complexity:	O(n)
# Space complexity:	O(n) (for list, O(log n) for call stack)
def reverse_order(node):
	if node == None:	#Driver function for root, eliminates an if per call
		return []
	res = []
	reverse_order_(node, res)
	return res

def reverse_order_(node, res):
	if node.right != None:
		reverse_order_(node.right, res)
	res.append(node.data)
	if node.left != None:
		reverse_order_(node.left, res)

		
# Description: 		Find node for element
# Improvements:		Don't use recursion
# Limitation:		Space usage for call stack
# Time complexity:	O(log n)
# Space complexity:	O(log n)	
def find_slow(root, element):
	if root == None:
		return None
		
	if element < root.data:
		return find_slow(root.left, element)
	elif element > root.data:
		return find_slow(root.right, element)
	else: # ==
		return root
		
		
# Description: 		Find element, without recursion
# Improvements:		None
# Limitation:		None
# Time complexity:	O(log n)
# Space complexity:	O(1)	
def find(root, element):
	res = root	
	while res != None:
		if element < res.data:
			res = res.left
		elif element > res.data:
			res = res.right
		else: 
			return res
	return None
				
		
		
def test():
	root = TreeNode(4)
	root.left = TreeNode(2)
	root.left.left = TreeNode(1)
	root.left.right = TreeNode(3)
	root.right = TreeNode(6)
	root.right.left = TreeNode(5)
	root.right.right = TreeNode(7)
	
	print(pre_order(root))
	print(in_order(root))
	print(post_order(root))
	print(reverse_order(root))
	print(find_slow(root, 7).data)
	print(find(root, 7).data)
		
		
		
		
		
		