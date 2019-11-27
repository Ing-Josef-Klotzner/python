#!/usr/bin/python3
# -*- coding: utf-8 -*-
from collections import deque

# find root for minimum height to tree (root = graph center)

# Graph is an undirected graph with adjacency list representation
class Graph:
    def __init__ (self, V):
        self.V = V
        self.adj = [[] for i in range (V + 1)]
        self.deg = [0 for i in range (V + 1)]
    def addEdge (self, v, w):
        self.adj [v].append (w) # Adds w to v's list
        self.adj [w].append (v) # Adds v to w's list
        self.deg [v] += 1	 # increment degree of v by 1
        self.deg [w] += 1	 # increment degree of w by 1
    # Method to return roots which gives minimum height to tree
    def rootForMinimumHeight (self):
        q = deque ()
        for i in range (self.V + 1):   # all leaves to queue
            if self.deg [i] == 1: q.append (i)
        while self.V > 2:
            for _ in range (len (q)):
                lv = q.popleft ()
                self.V -= 1
                for j in self.adj [lv]: # for all leave neighbours
                    print (self.adj [lv])
                    self.deg [j] -= 1
                    if self.deg [j] == 1: q.append (j)
        return q

# Driver code to test above methods
#g = Graph (6)
#g.addEdge (0, 3)
#g.addEdge (1, 3)
#g.addEdge (2, 3)
#g.addEdge (4, 3)
#g.addEdge (5, 4)
g = Graph (5)
g.addEdge (1, 3)
g.addEdge (2, 3)
g.addEdge (3, 4)
g.addEdge (4, 5)
res = g.rootForMinimumHeight ()
for i in res:
    print (i, end = ", ")
print ("are center nodes")
