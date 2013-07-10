
# Find lowest common ancestor to element A and B in a binary search tree

class TreeNode():
	left = None
	right = None
	data = None
	
	def __init__(self, data):
		self.data = data
	

# Description: 		Move down until divergence from max/min
# Improvements:		None
# Limitation:		None
# Time complexity:	O(log n)
# Space complexity:	O(1)
def ancestor(root, elementA, elementB):
	res = root
	minVal = min(elementA, elementB)
	maxVal = max(elementA, elementB)
	while res != None:
		if res.data > maxVal:
			res = res.left
		elif res.data < minVal:
			res = res.right
		else:
			return res
	return None
		


def test():
	root = TreeNode(5)
	root.left = TreeNode(3)
	root.left.left = TreeNode(2)
	root.left.right = TreeNode(4)
	root.right = TreeNode(7)
	root.right.left = TreeNode(6)
	root.right.right = TreeNode(8)
	return ancestor(root, 8, 6).data
	
	
	
	
	
	
	
	