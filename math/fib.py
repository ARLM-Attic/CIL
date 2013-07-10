
# Calculate Fibonacci number n

# Description: 		Uses recursion
# Improvements:		Don't use recursion
# Limitation:		Slow, O(n**2) and O(n) space for call stack
# Time complexity:	O(n**2)
# Space complexity:	O(n)
def fib_slow(n = 100):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

# Description: 		Uses loop
# Improvements:		O(log n) possible: https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
# Limitation:		Not optimal
# Time complexity:	O(n)
# Space complexity:	O(1)
def fib(n = 100):
	fibl = 0
	fibr = 1
	for i in range(2,n+1):
		fib = fibl + fibr
		fibl = fibr
		fibr = fib
	return fibr
	
	
	
	
	
	
