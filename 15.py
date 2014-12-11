
# Every path has M "rights" and N "downs", where M and N are the rows and columns of the grid, respectively.
# Every path is of steps M*N. How many strings can we have of that combination? Order doesn't matter,
# So not a permutation but a combination


import time

#def pathsInGrid(currPath, paths):
#	if paths == '':
#		print currPath
##	else:
#		for i in xrange(0, len(paths)):
#			remaining = paths[0:i] + paths[i+1:]
#			pathsInGrid(currPath + paths[i], remaining)

def factorial(n):
	if n is 0 or n is 1:
		return 1
	else:
		return n*factorial(n-1)

def binomial(n, k):
	return (factorial(n) / (factorial(k)*factorial(n - k)) )

if __name__ == "__main__":
	p = time.time()
	print binomial(2*20, 20)
	print time.time() - p #.09ms
	