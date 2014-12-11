def rankOfPermutation(s):
	# given a string, find the lexicographic rank of its permutation
	# i.e. if all permutations of s were sorted, in what place in the sorting would s come?
	rank = 0
	n = len(s)
	# there are n! permutations
	# there are n!/n or (n-1)! permutations for each letter coming first
	# we simply step down the string methodically, for each character seeing where that fits in the rank
	# as we prune down the rank
	step = factorial(n)
	for i in xrange(n):
		step /= (n-i)
		# to avoid dividing by zero
		# find smaller elements that occur after s[i] in the string, so we know what our next step is
		index = findSmallerInRight(s, i)

		# we lose a character here, so our step is goes down by a factor of n (i.e. we only have (n-1)! options now)
		# this is why we concatentate the string per below
		rank += index*step
	return rank + 1 # unless we want our rank to be zero-indexed

def findPermutation(s, rank):
	#given lexicographic rank, find the permutation of s of that rank.
	n = len(s)
	step = factorial(n)
	perm = ''
	s = sorted(s)
	for i in xrange(n):
		step /= (n-i)
		index = rank / step
		perm += s[index]
		del s[index]
		rank -= (index)*step
	return perm


def findSmallerInRight(s, i):
	count = 0
	elem = s[i]
	for i in xrange(len(s)-1, i, -1):
		if s[i] < elem:
			count += 1
	return count
