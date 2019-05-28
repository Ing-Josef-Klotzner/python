#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
input for a strike: 10,0
3,18,25
3,18
15
0,10,10
5,14,29,49,60,61,77,97,117,133
0,0,0,0,0,0,0,0,0,0
30,60,90,120,150,180,210,240,280,310
9,25,40,60,80,97,113,133,153,169
"""

# initial
# input of iterations (count of) and length (of one linesegment of triangle)

resultat = 0
z_erg = 0
last_throw_pair_count = 0
strike_count = 0
spare_count = 0
rounds = int(raw_input("Bitte geben sie die Anzahl der Runden ein: "))
total_throws = rounds * 2 + 1
counter = 1
throw = []
ergebnis = []
while counter <= total_throws:
	throw.append(int(raw_input("Bitte geben sie den Wurf ein: ")))
	counter = counter +1
#print "Runden:", rounds, throw 
#print " der sechste wurf ist ", throw[5]
counter = 1
while counter < total_throws:
	#print counter
	throw_pair_count = throw[counter-1]+throw[counter]
	#strike
	if throw[counter-1] == 10 and (counter+1 < total_throws):
		strike_count = throw[counter+1]
	if throw[counter-1] == 10 and (counter+2 < total_throws):
		strike_count = strike_count + throw[counter+2]
	if throw[counter-1] == 10 and (counter+3 < total_throws):
		if throw[counter+1] == 10:
			strike_count = strike_count + throw[counter+3]
	#spare
	if throw_pair_count == 10 and (counter+1 < total_throws) and strike_count == 0:
		spare_count = throw[counter+1]
	z_erg = strike_count + spare_count + throw_pair_count
	resultat = resultat + z_erg
	ergebnis.append(resultat)
	counter = counter + 2
	spare_count = 0
	strike_count = 0
print throw
print ergebnis
print resultat
