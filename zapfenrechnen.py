# zapfenrechnen
# -*- coding: iso-8859-15 -*-
print "Bitte geben sie die Ausgangszahl fuer den Zapfen ein: "
begin = int(raw_input())
print "Beginn: "
calc = begin
for x in range(2,10):
	print '%20d' % calc, " mal ",x
	calc = calc * x
for x in range(2,10):
	print repr(calc).rjust(20), " durch ", x
	calc = calc / x
print repr(calc).rjust(20)