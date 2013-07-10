
# Find one of the equilibrium points in an array
# An equilibrium point is where the sum of elements to the of the 
# point are equal to the sum of elements on the right

# Description: 		Simple loop from left
# Improvements:		Divide and conquer?
# Limitation:		None
# Time complexity:	O(n)
# Space complexity:	O(1)
def equilibrium(array = [0,1,2,3,4,-3,-2,-1,0]):
	sum = 0
	length = len(array)
	for i in range(length):
		sum += array[i]
	
	sumL = 0
	for i in range(length):
		sumR = sum - sumL - array[i]
		if sumR == sumL:
			return i
		sumL += array[i]

	return -1