# 1-10 times 10
# -*- coding: iso-8859-15 -*-
for x in range(1,11):
	print '%2d' % (x),
	print '%3d' % (x*x),
	print repr(x**3).rjust(4),
	print repr(x**4).rjust(5),
	print repr(x**5).rjust(6),
	print repr(x**6).rjust(7),
	print repr(x**7).rjust(8),
	print repr(x**8).rjust(9),
	print repr(x**9).rjust(10),
	print '%11d' % (x**10)
	