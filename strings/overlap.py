
# How many of the (case sensitive) characters in string A are in string B?

# Description: 		Uses dictionary (aka hash table)
# Improvements:		If we know the bounds on characters; use array
# Limitation:		Slow, if dictionary is too big to keep in RAM
# Time complexity:	O(n)
# Space complexity:	O(n)
def overlap(stringA = "Needles", stringB = "Haystack"):
	lengthB = len(stringB)
	lengthA = len(stringA)
	chars = {}
	for i in range(lengthB):
		chars[stringB[i]] = True #value irrelevant

	matches = 0
	for i in range(lengthA):
		if stringA[i] in chars:
			matches += 1
	return matches
	
