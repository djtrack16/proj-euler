#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Insight:

"""12 covers 2,3,4,6
14 covers 7
the primes: 11,13,15,17,19
20 covers 10 and 5
18 covers 9
16 covers 8

11-20 covers 1-10, the primes take care of themselves """

import time

primesOverTen = [19, 17, 13, 11]
compositesOverTen = [18, 16, 15, 14]

""" Returns the smallest positive number divisible by 1-20"""
def _smallest():
	x = 2660 # start at 2660 next largest number divisible by 19 and 20
	while(True):
		if (x % 12 is 0):
			if (divisibility(x, primesOverTen) and divisibility(x, compositesOverTen)):
				print x
				break
		# 19 is the largest "least divisible" number in this bunch
		# It is only divisible with 20 in increments of (20*19 = 380). 
		# So increment by 380 each time, but this means we must start off with a multiple of 19 (2660)
		# Now 16 times faster
		x += 380




# boolean for testing divisbility of composites and primes
def divisibility(num, arr):
	for i in arr:
		if (num % i != 0):
			return False
	return True

if __name__ == "__main__":
	s = time.time()
	_smallest()
	print time.time() - s