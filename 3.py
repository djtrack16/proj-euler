#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

import time

# Test by Trial Division
def isPrime(m):
	#end = int(m ** .5) + 1
	#if (m != 2 and m % 2 == 0): return False
	#for i in range(2, end):
	#	if (m % i == 0): return False

	#return True

	return not ( m < 2 or any( m % i is 0 for i in xrange(2, int(m**0.5) + 1)))

# Integer Factorization, the fundamental theorem of arithmetic
def primeFactors(n,factors):
	if(isPrime(n)): 
		factors.add(n)
		return

	for i in xrange(2, n):
		if ( n % i is 0):
			num = n / i
			primeFactors(num,factors)
			primeFactors(i,factors)
			return

if __name__ == "__main__":
	f = int(raw_input())
	for line in xrange(f):
		i = int(raw_input())
		p = set([])
		primeFactors(i, p)
		print max(p)