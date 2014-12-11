"""The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence (the difference between the sum of the squares of the first ten natural numbers and the square of the sum) is 3025-385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
import time
def sumOfSquares(limit):
	curr = 1 # 1^2 = 1
	step = 3
	sum = 1
	for i in xrange(2, limit + 1):

		curr += step # current perfect square
		step += 2 # what to increment, always the next odd number, 3 is the start
		sum += curr # sum of squares

	return sum



# A well known proof

# Sum(n) = (n(n+1))/2

def squaresOfSum(limit):
	return ( (limit*(limit + 1))/2)**2

if __name__ == "__main__":
	s = time.time()
	print squaresOfSum(100) - sumOfSquares(100)
	print time.time() - s