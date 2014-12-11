#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import time

def isPalindrome(s):
	#Check the end digits
	if (s is ''): return True
	if (s[0] is not s[-1]):
		return False
	# substring is from start index, up to but NOT including end index 
	return isPalindrome(s[1:-1])

def largestPalindromeFromTwoThreeDigitNumbers(limit):
	product = 0
	limit -= (limit%11)
	for i in xrange(limit, 10001,-99):
		if isPalindrome(str(i)):
			if divisibleBy(i):
				return i

def divisibleBy(i):
	# checks if divisible by 3 digit numbers
	for j in xrange(int(i**.5), 99, -1):
		if i%j==0:
			return True
	return False

		
		

	

if __name__ == "__main__":
	f = int(raw_input())
	for line in xrange(f):
		i = int(raw_input())
		print largestPalindromeFromTwoThreeDigitNumbers(i)
	