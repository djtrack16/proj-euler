import time

# A dict of the all the necessary numbers, returning 'None' as the default
def f(x):
	return {
		1: 'one',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five',
		6: 'six',
		7: 'seven',
		8: 'eight',
		9: 'nine',
		10: 'ten',
		11: 'eleven',
		12: 'twelve',
		13: 'thirteen',
		14: 'fourteen',
		15: 'fifteen',
		16: 'sixteen',
		17: 'seventeen',
		18: 'eighteen',
		19: 'nineteen',
		20: 'twenty',
		30: 'thirty',
		40: 'forty',
		50: 'fifty',
		60: 'sixty',
		70: 'seventy',
		80: 'eighty',
		90: 'ninety',
	}.get(x, None)

def summ():
	firstTen = 0
	nextTen = 0
	for i in xrange(1,20):
		# 1-9
		if i < 10:
			firstTen += len(f(i))
		# 10 - 20
		if i >= 10:
			nextTen += len(f(i))
	#20-99
	tens = 0
	for i in xrange(20, 100, 10):
		tens += len(f(i))
	# 10-19 + (20+30....+90)*10 + 8*(1-9)
	theFirstHundred = nextTen + tens*10 + firstTen*9
	# Don't forget the one thousand on the end
	print firstTen*100 + len('hundred')*900 + len('and')*891 + theFirstHundred*10 + len('onethousand')

s = time.time()	
summ()
print time.time() - s # less than 1ms