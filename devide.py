# devide - defining clean-up actions
#import sys
def devide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print "division by zero!"
	else:
		print "result is", result
	finally:                                                 # finally funktioniert in win python 2.4.4 nicht - aber in 2.5.2
		print "executing finally clause"
print "devide (2,1)"
devide(2,1)
print "devide (2,0)"
devide(2,0)
#print "devide ("2","1")"
#devide(2,1)
