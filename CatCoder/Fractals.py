#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
we start with an equilateral
triangle and replace the middle third of
every line segment with a pair of line
segments that form an equilateral
"bump".
Then perform the same replacement on every line
segment of the resulting shape, ad infinitum.
• Generation of koch snowflake
The objective here is to calculate the perimeter of the
resulting snowflake in each iteration for the given length
of equilateral triangle.
1242
114642
3095334
3147174
Samnit2
Lebenspunkte: 5140
Stärke: 264
Geschicklichkeit: 403
Beweglichkeit: 281
Konstitution: 146
Charisma: 183
Intelligenz: 181
Stufe 118
"""

# initial
# input of iterations (count of) and length (of one linesegment of triangle)

linesegment = int(raw_input("Bitte geben sie die Länge der Dreiecksseiten ein: "))
iterations = int(raw_input("Bitte geben sie die Anzahl der Iterationen ein: "))
counter = iterations

count_of_linesegments = 3
perimeter = linesegment * 3

while counter > 0:
	counter=counter-1
	perimeter = perimeter + count_of_linesegments * (linesegment/3)
#	print perimeter, count_of_linesegments, linesegment
	count_of_linesegments = count_of_linesegments * 2
	linesegment = linesegment/3
print "Resultat Umfang:",perimeter
