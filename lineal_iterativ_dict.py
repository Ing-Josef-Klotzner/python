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

lin_len=int (argv[1])
hight=int (argv[2])
hight_pos = hight
lineal = dict()
nenner = 2
while (lin_len / nenner > 2) :
    for zaehler in range(1, nenner, 2):   # nur ungerade Zähler um nur Zwischenräume zu erreichen
        lin_split = int(round(float(zaehler) * lin_len / nenner))
        lineal[lin_split] = hight_pos
        # print str(lin_split) +" "+str(hight_pos)
    nenner *= 2
    hight_pos -= 5

print
print ("Lineal als Dictionary mit welchem mit x-Wert als Schlüssel die definierten Strichlängen ausgelesen werden")
print lineal
print 

for i in range (1,lin_len+1) :
    if i in lineal :
        print "{:4}".format(i)+lineal[i]*"*"
    else :
        print "{:4}".format(i)+"."

