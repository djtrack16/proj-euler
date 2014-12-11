"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?"""

import time

def isPrime(m):
	return not ( m < 2 or any( m % i == 0 for i in xrange(2, int(m**0.5) + 1)))

# Key element is knowing how many primes are within 100 digits on average, keeping the iterations to a minimum
def nthPrime(n):
	if (n is 1): 
		return 2
	curr = 1
	n -= 1
	while(n > 0):
		curr += 2 # step 2 because we only need to do odd numbers
		if isPrime(curr):
			n -= 1
	return curr



if __name__ == "__main__":
	s = time.time()
	print nthPrime(10001)
	print 'Runtime: ' + str(time.time() - s) + 's' #650ms