# iterators 2 - reverse eingabe
#import sys
class Reverse:
	"Iterator for looping over a sequence backwards"
	def __init__(self, data):
		self.data = data
		self.index = len(data)
	def __iter__(self):
		return self
	def next(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]
print ("Bitte zu reversierenden Begriff eingeben: ")
ToReverse=raw_input()
for char in Reverse(ToReverse):
	print (char),
