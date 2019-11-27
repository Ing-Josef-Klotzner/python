# Measure some strings:
# -*- coding: iso-8859-15 -*-
for n in range(2, 30):
	noprime =  False
	for x in range(2, n):
		if n % x == 0:
			noprime = True
			if x <= n/x:
				print n, 'equals', x, '*', n/x
			if ((x >= (n/x)) and noprime == True):
#				print x,(n/x)
				break
	else:
		# loop fell through without finding a factor
		print n, 'is a prime number'
