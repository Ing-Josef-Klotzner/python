#! /usr/bin/env python2
from itertools import permutations

for p in permutations(['r','e','d']): print ''.join(p)
#for p in permutations(list("game")): print ''.join(p)
i,c=1,1
for p in permutations(list("Beispiel")): 
	c+=1
	i+=1
	if c==1000:
		print i,
		print ''.join(p)
		c=0
print "Anzahl von Permutationen "+str(i)