"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""

import time
from bitarray import bitarray # bitarray as a efficient way to store 2000000 numbers

# Brute force way
def isPrime(m):
	#Don't check even numbers, start at 3 and step 2
	return not ( m < 2 or any( m % i is 0 for i in xrange(3, int(m**0.5) + 1, 2)))

def allPrimesBelowLimit(start,limit, step):
	sum = 2 # start at 2 because we skip 2 in our loop
	for i in xrange(start, limit, step):
			if(isPrime(i)):
				sum += i
	return sum

# Sieve of Erasthonenes and using a bitarray of 2M bits ( ~250KB ) should be O(n) time
def allPrimesBelowLimitFast(limit):
	b = bitarray('1'*limit)
	sum = 0
	length = len(b)
	for index in xrange(2, length):

		# if index is False, not a prime, just move on
		if not b[index]:
			continue

		# cross out all multiples if not already crossed out, step by a multiple every time
		for multiple in xrange(index*2, length, index):
			if b[multiple]:
				b[multiple] = False

		#number is a prime if we get this far
		sum += index

	return sum	


if __name__ == "__main__":
	s = time.time()
	print allPrimesBelowLimit(1, 2000000, 2) #18 s
	print allPrimesBelowLimitFast(2000000) # 3s
	print time.time() - s