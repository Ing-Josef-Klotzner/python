#! /usr/bin/env python2
def permutations(items):
    n = len(items)
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield [items[i]]+cc

for p in permutations(['r','e','d']): print ''.join(p)
#for p in permutations(list("game")): print ''.join(p)
i=1
for p in permutations(list("Sportplatz")): 
	print i,
	print ''.join(p)
	i+=1