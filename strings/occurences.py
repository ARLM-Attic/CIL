
# Find the number of occurences of some character in a string, case-sensitive

# Description: 		Uses loop
# Improvements:		Use MapReduce if string is huge
# Limitation:		May not run well on a single machine for huge strings
# Time complexity:	O(n)
# Space complexity:	O(1)
def occurences(char = 'C', string = "ComprehensiveTestString"):
	counts = 0
	for i in range(len(string)):
		if string[i] == char:
			counts += 1
	return counts
