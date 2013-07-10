
# Find out if a string is a palindrome or not, without whitespace and ignoring case

# Description: 		Compare from both start and end
# Improvements:		None
# Limitation:		None
# Time complexity:	O(n)
# Space complexity:	O(1)
def palindrome(string = "Ni talar bra latin"):
	str = string.replace(' ', '').lower()
	length = len(str)-1
	half = length >> 1
	for i in range(half): # >> 1 = divide by 2
		if str[i] != str[length-i]:
			return False
	return True
	