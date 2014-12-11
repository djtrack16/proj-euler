import time
from math import sqrt

#The sequence of triangle numbers is generated by adding the natural numbers.
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#Let us list the factors of the first seven triangle numbers:
#What is the value of the first triangle number to have over five hundred divisors?

def firstTriangleNoWithGreaterThanNDivisors(n, step, triangularNumber):
	while(True):
		 factors = divisors(triangularNumber)
		 step += 1
		 if factors >= n:
		 	return triangularNumber
		 triangularNumber += step

#http://mathschallenge.net/index.php?section=faq&ref=number/number_of_divisors

def divisors(n):
	factors = 0
	for i in xrange(2, int(sqrt(n)) + 1):
		# Making a list and only taking half is the same as going up to the square root
		# but if number is a perfect square, we count it's sqrt twice (i.e. 10*10 is two divisors)
		# so use trial division by square root as limit
		# stop halfway because we know every divisor has a match
		
		# if factor, increment as appropriate
		if (n % i is 0):
			factors += 1

	if isPerfectSquare(n):
		return factors*2 + 1 # -1 because sqrt(n) is counted twice

	return factors*2 + 2 # , not a perfect square, just return2 for 1 and the number

def isPerfectSquare(n):
	s = str(sqrt(n))
	return s[s.index('.')+1:] is '0'


if __name__ == "__main__":
	s = time.time()
	print firstTriangleNoWithGreaterThanNDivisors(500, 10000, 50005000)
	print time.time() - s # 2s