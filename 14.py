
import time

def getChain(start, cache):
	next = start
	length = 1
	while (next > 1):
		next = nextTerm(next)
		# if already calculated, just stop here and return its length
		# Dynamic programming :P
		# One way to optimize is to find out how to rid duplicates in the cache and link the 'dup' to its correct length
		if next in cache:
			cache[start] = length + cache[next]
			return cache[start]
		#else:
		#	cache[next] = 


		length += 1


	cache[start] = length
	return length
		

def nextTerm(n):
	if n % 2 is 0:
		return n/2
	else:
		return 3*n + 1


# 20 times faster with the cache
def longestChain(start, limit, cache):
	longest = 0
	num = 0
	# Would only look through odd numbers, but I need my even numbers to be in the cache also
	for i in xrange(start, limit, 2):
		curr = getChain(i, cache)
		#print i, cache
		if curr > longest:
			num = i
			longest = curr

		
	print '%d has a chain of %d elements until ending in 1' % (num, longest)

if __name__ == "__main__":
	s = time.time()
	longestChain(1, 1000000, {})
	print time.time() - s #5s