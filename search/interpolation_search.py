import array

# Interpolation search

# Description: 		Interpolation search using loop
# Improvements:		None
# Limitation:		None
# Time complexity:	O(log log n) (assuming reasonable distribution)
# Space complexity:	O(1)
def interpolation_search(value = 3, data = array.array('i', [i for i in range(10000)])):
	start = 0
	end = len(data)-1
	
	while data[start] <= value and data[end] >= value and start < end:
		mid = int(start + ((value - data[start]) * (end - start)) // (data[end] - data[start]))
		
		if data[mid] < value:
			start = mid+1
		elif data[mid] > value:
			end = mid-1
		else:
			return mid
			
	if data[start] == value:	# if we broke cause start == end
		return start		
	return -1
	
	
	
def test():
	import random
	vals = array.array('f', [random.random()])
	length = 10000
	for i in range(1,length):
		vals.append(random.random() + vals[i-1])
	for i in range(1000):
		val = vals[int(random.random()*length)]
		if interpolation_search(val, vals) < 0:
			return "Error"
	if interpolation_search(-1, vals) >= 0:
		return "Error"
	if interpolation_search(length, vals) >= 0:
		return "Error"
	return "Correct"
			
			
			
			
			
			