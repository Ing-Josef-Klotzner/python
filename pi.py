#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#pi=3.14159265359
n=10000   #Anzahl Terme einer Reihenentwicklung von Pi nach Gottfried Wilhelm Leibnitz
b=1
val=1.0
print "1  Terme ",val
while b < n-1:
	val-=1.0/(b*2+1)
	print b+1," Terme ",val
	last=val
	val+=1.0/(b*2+3)
	print b+2," Terme ",val
	b+=2
print "Pi ist ",(last+val)*2," mit ",n," Termen Berechnung"
# Ergebnis von Pi ist  3.14159264859  mit  10000  Termen Berechnung
