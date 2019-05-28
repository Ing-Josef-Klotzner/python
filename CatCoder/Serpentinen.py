#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Beispiel 1:
Eingabe: 3 4
Ausgabe: 1 2 3 4 8 7 6 5 9 10 11 12
Beispiel 2:
Eingabe: 5 2
Ausgabe: 1 2 4 3 5 6 8 7 9 10

"""
rows = int(raw_input("Bitte geben sie die Anzahl der Reihen ein: "))
columns = int(raw_input("Bitte geben sie die Anzahl der Spalten ein: "))
counter = 0
counter2 = 0
row = []
finalrow = []

while counter < rows:
	while counter2 < columns:
		row.append(counter*(columns)+(counter2+1))
		counter2 = counter2 +1
	if ((counter+2) % 1) == 0:
		row.reverse()
	finalrow = finalrow + row
	counter = counter +1
	counter2 = 0
	row = []
for x in finalrow:
	print x,
#print finalrow
"""


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
"""
