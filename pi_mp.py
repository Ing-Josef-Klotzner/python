#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from __future__ import absolute_import, division, print_function
#pi=3.14159265359     Berechnung more precise
n=600 #Anzahl Terme
b=1
val=1.0
print("1  Terme ",val," ",val*4)
while b < n-1:
    val-=1./(b*2+1)
    print(b+1," Terme ",val," ",val*4)
    last=val
    val+=1./(b*2+3)
    print(b+2," Terme ",val," ",val*4)
    b+=2
b-=2
print("Pi ist ueber 2 Terme gemittelt ",(last+val)*2," mit ",n," Termen Berechnung")
print("Pi ist ueber Methodik gewichtete Termenanteilruecknahme ")
print(4.*(val-1.0/(b*2.+3.)*(b*2.+1.)/((b*2.+3.)+(b*2.+1.))))
print("Pi ist ueber Methodik gewichtete Termenanteilruecknahme ueber 2 gemittelt ")
print(2.*((val-1.0/(b*2.+3.)*(b*2.+1.)/((b*2.+3.)+(b*2.+1.)))+(last+1.0/(b*2.+1.)*(b*2.-1.)/((b*2.+1.)+(b*2.-1.)))))
# Ergebnis von Pi ist  3.14159264859  mit  10000  Termen Berechnung