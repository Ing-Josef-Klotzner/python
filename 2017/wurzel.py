#!/usr/bin/python
# -*- coding: utf-8 -*

import operator
fst = operator.itemgetter (0)
snd = operator.itemgetter (1)

def wurzel(x): return wurzeliter(1.0,x,0)
def wurzeliter(schaetzwert,x,z):
	if gutgenug(schaetzwert,x):
		return (schaetzwert, z)
	else: 
		print (schaetzwert, x)
		return wurzeliter (verbessern (schaetzwert, x), x, z + 1)
def quadrat(x): return x*x
def gutgenug (schaetzwert,x):
	return (abs ((quadrat(schaetzwert) - x) / x) <= 0.00000000001)
def verbessern (schaetzwert,x):
	return mittelwert (schaetzwert, (x / schaetzwert))
def mittelwert (x,y): return (x + y) / 2.0

def main ():
	print ("Wurzel zu berechnen von: ")
	in_ = input ()
	erg = wurzel (in_)
	print ("Wurzel: ", fst (erg),\
		"Rekursionen hierzu: ", snd (erg))

if __name__ == "__main__":
    main()
