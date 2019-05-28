#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Beispiel 1:
Eingabe: 3 4 1 1 S
Ausgabe: 1 5 9 10 6 2 3 7 11 12 8 4
Beispiel 2:
Eingabe: 5 2 5 2 N
Ausgabe: 10 8 6 4 2 1 3 5 7 9

"""
rows = int(raw_input("Bitte geben sie die Anzahl der Reihen ein: "))
columns = int(raw_input("Bitte geben sie die Anzahl der Spalten ein: "))
rows_begin = int(raw_input("Bitte geben sie die Beginn-Reihe ein: "))
columns_begin = int(raw_input("Bitte geben sie die Beginn-Spalte ein: "))
direction = raw_input("Bitte geben sie H für horizontales und V für vertikales befahren ein: ")
counter = 0
counter2 = 0
row = []
finalrow = []
mod_nr = 1
if direction == "H" or direction == "h":
	if (rows_begin == 1 and columns_begin == columns)or(rows_begin == rows and columns_begin == columns):
		mod_nr = 0
if direction == "V" or direction == "v":
	if (rows_begin == rows and columns_begin == 1)or(rows_begin == rows and columns_begin == columns):
		mod_nr = 0

if direction == "H" or direction == "h" and ((rows_begin == 1 and columns_begin == 1) or (rows_begin == 1 and columns_begin == columns)):
	while counter < rows:
		while counter2 < columns:
			row.append(counter*(columns)+(counter2+1))
			counter2 = counter2 +1
		if ((counter+2) % 2) == mod_nr:
			row.reverse()
		finalrow = finalrow + row
		counter = counter +1
		counter2 = 0
		row = []
counter = rows-1
if direction == "H" or direction == "h" and ((rows_begin == rows and columns_begin == columns) or (rows_begin == rows and columns_begin == 1)):
	while counter >= 0:
		while counter2 < columns:
			row.append(counter*(columns)+(counter2+1))
			counter2 = counter2 +1
		if ((counter+2) % 2) == mod_nr:
			row.reverse()
		finalrow = finalrow + row
		counter = counter -1
		counter2 = 0
		row = []
counter = 0
if direction == "V" or direction == "v" and ((rows_begin == 1 and columns_begin == 1) or (rows_begin == rows and columns_begin == 1)):
	while counter < columns:
		while counter2 < rows:
			row.append(counter2*(columns)+(counter+1))
			counter2 = counter2 +1
		if ((counter+2) % 2) == mod_nr:
			row.reverse()
		finalrow = finalrow + row
		counter = counter +1
		counter2 = 0
		row = []
counter = columns-1
if direction == "V" or direction == "v" and ((rows_begin == rows and columns_begin == columns) or (rows_begin == 1 and columns_begin == columns)):
	while counter >= 0:
		while counter2 < rows:
			row.append(counter2*(columns)+(counter+1))
			counter2 = counter2 +1
		if ((counter+2) % 2) == mod_nr:
			row.reverse()
		finalrow = finalrow + row
		counter = counter -1
		counter2 = 0
		row = []

for x in finalrow:
	print x,
