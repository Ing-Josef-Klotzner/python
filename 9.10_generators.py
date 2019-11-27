# generators - reverse eingabe
#import sys
def reverse(data):
	for index in range(len(data)-1, -1, -1):
		yield data[index]

print "Bitte zu reversierenden Begriff eingeben: "
ToReverse=raw_input()
for char in reverse(ToReverse):
	print char,