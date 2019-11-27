#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
from operator import itemgetter

# Benutzereingaben bei Programmaufruf prüfen
if len(argv) == 1 or len(argv) == 2 :
    print ("usage: "+argv[0]+" [Länge] [Strichhöhe]")
    print ("Es wird per default ein Lineal mit 1000 Länge und Strichhöhe 50 erstellt")
    print ("Ergebnis am besten in eine Datei umlenken z.B.: " + argv[0] + " > test.txt")
    argv.append ('1000')
    argv.append ('50')

lin_len = int (argv[1])
hight = int (argv[2])

def f_lineal(l,r,h, lineal = {}) :
    step = 5
    if ( h < 15 ) : 
        return
    else :
        m = ( l + r ) / 2
        lineal[m] = h
        f_lineal(l,m,h-step)
        f_lineal(m,r,h-step)
    return (lineal)

print
print ("Lineal als Dictionary mit welchem mit x-Wert als Schlüssel die definierten Strichlängen ausgelesen werden")
lineal = f_lineal ( 0, lin_len, hight ) 
print lineal
print


for i in range (1,lin_len+1) :
    if i in lineal :
        print "{:4}".format(i)+lineal[i]*"*"
    else :
        print "{:4}".format(i)+"."
