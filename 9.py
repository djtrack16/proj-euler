"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""
import time
#from math import sqrt

def findTriplet():
	# Find the upper and lower bounds.
	# Lower bound: 100 is good 
	# Upper bound: None above 400 because 400+401+((400^2+401^2))**.5 > 1000
	# The set of numbers is strictly increasing
	# 
	sum = 0
	for i in xrange(100, 400):
		for j in xrange(i+1, 400):
			sum = i**2 + j**2
			sqrt = sum**.5
			if( isPerfectSquare(str(sqrt)) and ((i + j + int(sqrt)) == 1000)):
				return i*j*sqrt, i, j, sqrt

# because sqrt or **.5 always returns a float, just look for single '.0' at end of string
def isPerfectSquare(s):
	return s[s.index('.')+1:] is '0'

if __name__ == "__main__":
	s = time.time()
	print findTriplet()
	print time.time() - s #49ms
