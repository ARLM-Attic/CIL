
# Integer division without division operator

# Description: 		Loop with minus
# Improvements:		Bitwise techniques
# Limitation:		Takes linear time
# Time complexity:	O(n)
# Space complexity:	O(1)
def division_slow(value = 10, dividend = 2):
	if dividend == 0:
		return float('NaN')
	
	remainder = abs(value)
	div = abs(dividend)
	result = 0
	while remainder >= div:
		remainder -= div
		result += 1
	return result
	

# Description: 		Bitwise technique
# Improvements:		None
# Limitation:		None
# Time complexity:	O(k)
# Space complexity:	O(1)
def division_slow(value, dividend):
	pass