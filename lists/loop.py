
#Find the position of a loop in a singly linked list

class ListNode():
	next = None
	data = None
	
	def __init__(self, data):
		self.data = data;
		
		
# Description: 		Step two pointers with different speeds
# Improvements:		None
# Limitation:		Linear time
# Time complexity:	O(n)
# Space complexity:	O(1)
def loop(root):
	if root == None:
		return -1	# -1 = no loop
	
	node1 = root
	node2 = root.next
	steps = 0	
	while node1 != None and node2 != None:
		if node2.next == None:
			return -1 # can't be loop if we got to end of list
		node1 = node1.next
		node2 = node2.next.next
		steps += 1
		if node2 == node1:
			return steps
			
	return -1


def test():
	n1 = ListNode(0)		
	n2 = ListNode(1)
	n3 = ListNode(2)
	n1.next = n2
	n2.next = n3
	n3.next = n1
	return loop(n1)
	
	
	
	
	
	
		
		
		
		