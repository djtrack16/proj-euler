#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2^1000?

import time
# takes a base raised to exp and finds the sum of its digits
def sumOfDigits(base, exp):
	n = str(base**exp)
	count = 0
	for i in n:
		count += int(i)
	del n
	return count


if __name__ == "__main__":
	p = time.time()
	c = 2**1000
	print sumOfDigits(2, 1000)
	print time.time() - p