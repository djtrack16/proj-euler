#Solutions to projecteuler.net problems

#1

"""If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""


#insight
#3M is the set of multiples of 3
#5M is the set of multiples of 5
#answer is simply multiples of 3 plus multiples of 5 minus the intersection of the two (i.e. multiples of 15)
# answer is simply 3M + 5M - (the intersection 5M and 3M = 15M)
#upper limit in this case is 1000
#limit is L

# the sum of multiples of any n up to L = n * (summation from 1<=i<=k for all i where k = L/n Note: if l % n == 0, subract 1)
# well-known summation identity for all int from 1 to n: n*(n+1)/2
# so final, equation where k = L/n is n*(k*(k+1)/2)

# so, 3M + 5M - 15M
# solution now trivial and much faster than brute force

def getMultiples(num):
	# we take off 1 because we only want up to N, and if 3/5/15 is a perfect divisor of n, we don't want n
	three = num/3 if num % 3 != 0 else num/3-1
	five = num/5 if num % 5 != 0 else num/5-1
	fifteen = num/15 if num % 15 != 0 else num/15-1
	threeM = 3*(three*(three+1)/2)
	fiveM = 5*(five*(five+1)/2)
	fifteenM = 15*(fifteen*(fifteen+1)/2)
	return threeM + fiveM - fifteenM

if __name__ == '__main__':
	f = int(raw_input())
	for line in xrange(f):
		num = int(raw_input())
		print getMultiples(num)

