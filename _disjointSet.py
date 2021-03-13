#!/bin/python3

import os

# Python3 program to implement Disjoint Set Data  Structure. 
class DisjSet:
    def __init__ (self, n):
        # Constructor to create and initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range (n)]
        # all representatives and their set count {rep: count}
        self.reps = dict ([(x, 1) for x in range (n)])
    # Finds set (representative) of given item x
    def find (self, x):
        if self.parent [x] != x:
            # if x is not the parent of itself -> x not representative
            self.parent [x] = self.find (self.parent [x])
            # so we recursively call Find on its parent and move i's
            # node directly under the representative of this set
        return self.parent [x]
    # Do union of two sets represented by x and y.
    def union(self, x, y):
        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)
        # If they are already in same set
        if xset == yset: return
        # Put smaller ranked item under bigger ranked item
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
            self.reps [yset] += self.reps [xset]
            del self.reps [xset]
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
            self.reps [xset] += self.reps [yset]
            del self.reps [yset]
        # If ranks are same, then move y under x (doesn't matter
        # which one goes where) and increment rank of x's tree
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1
            self.reps [xset] += self.reps [yset]
            del self.reps [yset]

# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    ds = DisjSet (n)
    for a in astronaut:
        ds.union (*a)
    res = n * (n - 1) // 2
    for x in ds.reps.values ():
        res -= x * (x - 1) // 2
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
data for test:
5 3
0 1
2 3
0 4
"""
