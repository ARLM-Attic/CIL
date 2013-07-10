
# Reverse a string in-place


# Description: 		In-place
# Improvements:		Make use of clever pre-fetching
# Limitation:		Slow, if string is fetched from disk
# Time complexity:	O(n)
# Space complexity:	O(1)
def reverse(string = array.array('u', "The String to Reverse")):
	length = len(string)
	if length < 2:
		return string
	posl = 0
	posr = length-1
	while posl < posr:
		tmp = string[posl]
		string[posl] = string[posr]
		string[posr] = tmp
		posl += 1
		posr -= 1
	return string.tounicode()