#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Beispiel 1:
Eingabe: 3 4 1 4 S Z
Ausgabe: 4 8 12 9 5 1 3 7 11 10 6 2
Beispiel 2:
Eingabe: 5 2 5 2 N Z
Ausgabe: 10 8 6 4 2 1 3 5 7 9

"""
rows = int(raw_input("Bitte geben sie die Anzahl der Reihen ein: "))
columns = int(raw_input("Bitte geben sie die Anzahl der Spalten ein: "))
rows_begin = int(raw_input("Bitte geben sie die Beginn-Reihe ein: "))
columns_begin = int(raw_input("Bitte geben sie die Beginn-Spalte ein: "))
direction = raw_input("Bitte geben sie H für horizontales und V für vertikales befahren ein: ")
zirkular = raw_input("Bitte geben sie Z für zirkulares und N für normales befahren ein: ")
counter = 0
counter2 = 0
row = []
finalrow = []
mod_nr = 1
def circle(z):
	length = len(z)
	a = 1
	b = length
	c = 1
	y = list(z)
	while a <= b:
		y[c-1] = z[a-1]
		if a <> b:
			y[c] = z[b-1]
		c = c + 2
		a = a + 1
		b = b - 1
	return y
# counter = range(columns,0,-1)
if direction == "H" or direction == "h":
	if (rows_begin == 1 and columns_begin == columns)or(rows_begin == rows and columns_begin == columns):
		mod_nr = 0
	counter = range(1,columns+1)
#counter = 0
if direction == "V" or direction == "v":
	if (rows_begin == rows and columns_begin == 1)or(rows_begin == rows and columns_begin == columns):
		mod_nr = 0

if direction == "H" or direction == "h" and ((rows_begin == 1 and columns_begin == 1) or (rows_begin == 1 and columns_begin == columns)):
	counter = range (1, rows + 1)
	counter_nr = 0
	if zirkular == "Z" or zirkular =="z":
		counter = circle(counter)
	for i in counter:
		while counter2 < columns:
			row.append((i + 1)*(columns)+(counter2+1))
			counter2 = counter2 +1
		if ((counter_nr+1) % 2) == mod_nr:
			row.reverse()
		finalrow = finalrow + row
		counter_nr = counter_nr + 1
		counter2 = 0
		row = []
#counter = rows-1
if direction == "H" or direction == "h" and ((rows_begin == rows and columns_begin == columns) or (rows_begin == rows and columns_begin == 1)):
	counter = range (rows,0,-1)
	counter_nr = rows - 1
	if zirkular == "Z" or zirkular =="z":
		counter = circle(counter)
	for i in counter:
		while counter2 < columns:
			row.append((i + 1)*(columns)+(counter2+1))
			counter2 = counter2 +1
		if ((counter_nr+1) % 2) == mod_nr:
			row.reverse()
		finalrow = finalrow + row
		counter_nr = counter_nr -1
		counter2 = 0
		row = []
#counter = 0
if direction == "V" or direction == "v" and ((rows_begin == 1 and columns_begin == 1) or (rows_begin == rows and columns_begin == 1)):
	counter = range (1,columns +1)
	counter_nr = 0
	if zirkular == "Z" or zirkular =="z":
		counter = circle(counter)
	for i in counter:
		while counter2 < rows:
			row.append(counter2*(columns)+(i))
			counter2 = counter2 +1
		if ((counter_nr) % 2) == mod_nr:
			row.reverse()
		finalrow = finalrow + row
		counter_nr = counter_nr + 1
		counter2 = 0
		row = []
#counter = columns-1
if direction == "V" or direction == "v" and ((rows_begin == rows and columns_begin == columns) or (rows_begin == 1 and columns_begin == columns)):
	counter = range (columns,0,-1)
	counter_nr = columns - 1
	if zirkular == "Z" or zirkular =="z":
		counter = circle(counter)
	for i in counter:
		while counter2 < rows:
			row.append(counter2*(columns)+(i))
			counter2 = counter2 +1
		if ((counter_nr+1) % 2) == mod_nr:
			row.reverse()
		finalrow = finalrow + row
		counter_nr = counter_nr - 1
		counter2 = 0
		row = []

for x in finalrow:
	print x,
