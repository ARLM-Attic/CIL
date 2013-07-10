
# Find all prime numbers below a limit

# Description: 		The simple way
# Improvements:		Use sieve of Eratosthenes: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# Limitation:		Time complexity bad for large limits
# Time complexity:	O(n**2)
# Space complexity:	O(n)
def primes_slow(limit = 1000):
	primes = []
	for i in range(2,limit+1):
		for div in range(2, i):
			if i % div == 0:
				break
		else: #weird syntax, I know
			primes.append(i)
	return primes
				
		
# Description: 		Sieve of Eratosthenes
# Improvements:		There are faster algorithms: http://en.wikipedia.org/wiki/Sieve_of_Atkin
# Limitation:		Space complexity typically worse than time-complexity
# Time complexity:	O(n*log log n)
# Space complexity:	O(n)
def primes(limit = 1000):
	import math
	primes = [1 for i in range(limit)]
	primes[0] = 0
	primes[1] = 0
	i = 2
	end = math.sqrt(limit)
	while i < end:
		if primes[i] == 1:
			val = i**2
			while val < limit:
				primes[val] = 0
				val += i
		i += 1
	i = 0
	deleted = 0
	while i < len(primes):
		if primes[i] == 0:
			del primes[i]
			deleted += 1
		else:
			primes[i] = i+deleted
			i += 1
	return primes
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	