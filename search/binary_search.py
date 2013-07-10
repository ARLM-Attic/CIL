import array

# Binary search

# Description: 		Binary search using recursion
# Improvements:		Use loop
# Limitation:		Space for very large array
# Time complexity:	O(log n)
# Space complexity:	O(log n)
def binary_search(value = 3, data = array.array('i', [i for i in range(10000)])):
	length = len(data)
	if array == None or length == 0:
		return -1
	return binary_search_r(value, data, 0, length)
	
def binary_search_r(value, data, start, end):
	if start > end or start == len(data):
		return -1

	mid = (start+end) >> 1 	# x >> 1 = x // 2	
	if value < data[mid]:
		return binary_search_r(value, data, start, mid-1)
	elif value > data[mid]:
		return binary_search_r(value, data, mid+1, end)
	elif value == data[mid]:
		 return mid
	else:
		return -1
		
		
		
# Description: 		Binary search using loop
# Improvements:		Interpolation search
# Limitation:		None
# Time complexity:	O(log n)
# Space complexity:	O(1)
def binary_search_loop(value = 3, data = array.array('i', [i for i in range(10000)])):
	start = 0
	length = len(data)
	end = length
	
	while start <= end and start < length:
		mid = (start+end) >> 1 # x >> 1 = x // 2
		if value < data[mid]:
			end = mid-1
		elif value > data[mid]:
			start = mid+1
		elif value == data[mid]:
			return mid
	return -1
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	