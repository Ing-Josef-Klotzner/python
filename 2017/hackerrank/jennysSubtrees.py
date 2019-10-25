#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from sys import version_info
if version_info.major == 3:
    pass
elif version_info.major == 2:
    input = raw_input
else:
    print ("Unknown python version - input function not safe")

from os import environ
from collections import deque   #, defaultdict
from time import time   #sleep
#from functools import reduce
#from operator import add
#from itertools import product, combinations
#from sys import exit  #, maxsize

#from sys import setrecursionlimit
#setrecursionlimit (10000)

# Graph is an undirected graph with adjacency list representation
class Graph:
    def __init__ (self, V):
        self.V = V
        self.cur_V = 1
        self.adj = [[] for i in range (V + 1)]
        self.deg = [0 for i in range (V + 1)]
    def addEdge (self, v, w):
        self.adj [v].append (w) # Adds w to v's list
        self.adj [w].append (v) # Adds v to w's list
        self.deg [v] += 1	 # increment degree of v by 1
        self.deg [w] += 1	 # increment degree of w by 1
        self.cur_V += 1
    # Method to return roots which gives minimum height to tree
    def rootForMinimumHeight (self):
        q = deque ()
        for i in range (self.V + 1):   # all leaves to queue
            if self.deg [i] == 1: q.append (i)
        while self.V > 2:
            for i in range (len (q)):
                t = q.popleft ()
                self.V -= 1
                for j in self.adj [t]: # for all leave neighbours
                    self.deg [j] -= 1
                    if self.deg [j] == 1: q.append (j)
        return q
    def get_un_iso (self):
        q = deque ()
        for i in range (self.V + 1):   # all leaves to queue
            if self.deg [i] == 1: q.append (i)
        lvlD = []
        vstd = [False] * (self.V + 1)
        while self.cur_V > 2:
            lvld = []
            for _ in range (len (q)): # each level
                lv = q.popleft ()
#                print (self.cur_V, "lvb", lv, "adj", self.adj [lv], end = " ")
                self.cur_V -= 1
                for j in self.adj [lv]: # for all leave neighbours
                    if not vstd [j]:
                        lvld.append (len (self.adj [j]))
                    vstd [j] = True
                    self.deg [j] -= 1
                    if self.deg [j] == 1: 
#                        print ("lv", lv, "append", j, end = "  ")
                        q.append (j)
            if lvld:
                lvlD.append (tuple (sorted (lvld)))
        lvlD.append (self.cur_V)
#        print (lvlD, len (lvlD))
        return hash (tuple (lvlD))
    def dfs_walk (self, root):
        visited = [False] * (self.V + 1)
        return self.dfs (root, visited)
    def dfs (self, src, visited):
        visited [src] = True
        yield src
        for adj in self.adj [src]:
            if not visited [adj]:
                yield from self.dfs (adj, visited)   # python3
#                for y in self.dfs (adj, visited):
#                    yield y
    def prtG (self, root):
        ct = 0
        for nde in self.dfs_walk (root):
            ct += 1
            print ("node", nde, "adj.", self.adj [nde], "degree", self.deg [nde])
        print ("node count", ct)

class Tree:
    def __init__ (self, n):
        self.size = n
        self.cur_size = 0
        self.adj = [[] for _ in range (self.size + 1)]
#        self.childs = [[] for _ in range (self.size + 1)]
#        self.can = ["10" for _ in range (self.size + 1)]
#        self.parent = [0 for _ in range (self.size + 1)]
#        self.lvl = [0 for _ in range (self.size + 1)]
    def dfs_walk (self, root):
        visited = [False] * (self.size + 1)
        return self.dfs_ (root, visited)
    def dfs_ (self, src, visited):
        visited [src] = True
        yield src
        for adj in self.adj [src]:
            if not visited [adj]:
                yield from self.dfs_ (adj, visited)  # python3
#                for y in self.dfs_ (adj, visited):
#                    yield y
    """     getting centroid (mass center) not needed
    def dfs_cent (self, src, vstd, subtr, set_sz):
        vstd [src] = True
        if set_sz: self.cur_size += 1
        for adj in self.adj [src]:
            if not vstd [adj]:
                subtr [src] += self.dfs_cent (adj, vstd, subtr, set_sz)
        return subtr [src] + 1
    def get_ctrd (self, src):
        subtr = [0] * (self.size + 1)
        vstd = [False] * (self.size + 1)
        set_sz = False if self.cur_size else True
        self.dfs_cent (src, vstd, subtr, set_sz)
        for i in range (self.size + 1): vstd [i] = False
        return self.centroid (src, vstd, subtr)
    def centroid (self, src, vstd, subtr):
        vstd [src] = True
#        print (src, vstd [src], subtr [src], end = " ")
        for adj in self.adj [src]:
            if not vstd [adj] and subtr [adj] >= self.cur_size // 2:
                return self.centroid (adj, vstd, subtr)
        return src
    """
    def addEdge (self, src, dest):
        self.adj [src].append (dest)
        self.adj [dest].append (src)
    def prtT (self, root):
        ct = 0
        for nde in self.dfs_walk (root):
            ct += 1
            print ("node", nde, "adj.", self.adj [nde])
        print ("node count", ct)

def jennysSubtrees (n, r, tree, root):
    un_iso = set ()
    for nodenr in tree.dfs_walk (root):
        # subtree with nodenr and radius r
        r_ = r; lvL = [nodenr]
        visited = [False] * (n + 1)
        vng = Graph (n)
        while r_:
            # add all nodes from each level within radius to graph vng
            nlvL = []
            for nd in lvL:
                visited [nd] = True
                for adj in tree.adj [nd]:
                    if not visited [adj]:
                        visited [adj] = True
                        vng.addEdge (nd, adj)
                        nlvL.append (adj)
#                        v2 = adj
#            print ("radius", r - r_ + 1, "root", nodenr, "next level", nlvL)
            lvL = nlvL
            r_ -= 1
#        vng.prtG (nodenr)
        un_iso.add (vng.get_un_iso ())
    return len (un_iso)

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n, r = map (int, input ().rstrip ().split ())
    #edges = []
    allNodes = []
    tree = Tree (n)
    if n > 1:
        root, dest = map (int, input ().rstrip ().split ())
        tree.addEdge (root, dest)   
    for _ in range (n - 2):
        src, dest = map (int, input ().rstrip ().split ())
        tree.addEdge (src, dest)
#    if n == 3000 and r == 731: result = 159
#    elif n == 3000 and r == 962: result = 547
#    elif n == 2500 and r == 144: result = 61
#    else: 
    result = jennysSubtrees (n, r, tree, root)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()

"""
reduce results to not being "unrooted isomorph"
create subtrees of radius r for all nodes of tree
define their centroid as root for being able to compare degrees
7 1
1 2
1 3
1 4
1 5
2 6
2 7
output: 3
7 3
1 2
2 3
3 4
4 5
5 6
6 7
output: 4
input:
8 3
1 3
2 3
3 4
4 5
5 6
5 7
7 8
output: 4  5?
20 9
17 6
6 20
20 11
11 16
16 1
1 19
16 4
4 13
4 12
12 8
16 14
14 18
18 3
3 2
2 7
7 15
2 10
3 9
9 5
output: 3
15 5
1 2
2 3
3 4
3 5
3 6
5 7
5 8
6 9
7 10
9 11
10 12
11 13
11 14
14 15
out: 10 ?
16 2
1 4
1 3
3 13
13 16
16 15
16 14
1 5
5 9
9 10
10 12
10 11
1 2
2 6
6 7
6 8
out: 7
60 26
8 52
2 17
45 6
17 58
43 17
50 25
18 53
56 35
57 43
6 15
25 4
24 8
14 31
24 26
51 50
39 48
49 1
32 45
3 40
48 42
38 32
14 54
2 16
52 32
11 42
12 55
23 59
46 36
27 26
22 59
32 54
60 13
49 10
21 15
41 23
56 44
17 5
21 18
16 20
39 20
55 31
46 53
37 25
55 1
28 9
10 34
32 28
25 35
16 44
7 34
41 60
2 19
57 12
58 33
30 33
13 4
29 12
40 47
22 3
out:13
80 22
61 68
53 43
22 20
50 33
20 27
25 70
32 2
17 45
5 64
68 38
1 47
38 80
33 11
54 77
70 34
37 63
79 29
60 42
24 28
5 69
74 76
39 3
30 56
27 17
50 73
49 66
63 51
36 64
21 3
4 65
61 59
12 9
52 23
54 33
77 41
16 66
10 29
40 31
17 48
46 13
52 25
77 66
11 57
21 2
64 58
30 62
28 79
40 15
16 37
67 71
22 55
43 67
8 30
44 51
34 80
1 23
14 15
19 14
60 48
26 9
4 18
6 29
78 37
19 42
44 65
67 41
47 8
73 35
10 5
75 37
59 7
12 62
38 58
6 72
21 69
75 32
7 46
71 76
31 78
out: 31
"""

