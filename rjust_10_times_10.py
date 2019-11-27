# 1-10 times 10
# -*- coding: iso-8859-15 -*-
for x in range(1,11):
	print repr(x).rjust(2),
	print repr(x*x).rjust(3),
	print repr(x*x*x).rjust(4),
	print repr(x*x*x*x).rjust(5),
	print repr(x*x*x*x*x).rjust(6),
	print repr(x*x*x*x*x*x).rjust(7),
	print repr(x*x*x*x*x*x*x).rjust(8),
	print repr(x*x*x*x*x*x*x*x).rjust(9),
	print repr(x*x*x*x*x*x*x*x*x).rjust(10),
	print repr(x*x*x*x*x*x*x*x*x*x).rjust(11)
	