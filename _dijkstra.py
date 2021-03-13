#!/bin/python3

from os import environ
from sys import stdin, maxsize
from collections import defaultdict
 
class Graph():
    def __init__(self, vertices, edges, edists):
        self.V = vertices
        self.edges = edges
        self.edists = edists
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance (self, dist, rsnwd):
        # Initilaize minimum distance for next node
        min = maxsize
        # Search vertex with smallest distance from restSet rsnwd
        for v in rsnwd:
            if dist [v] < min:
                min = dist [v]
                min_index = v
        return min_index
    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src, restSet):
        dist = [maxsize] * (self.V + 1)
        dist [src] = 0
        #restSet = set (list (range (1, self.V + 1)))
        rsnwd = {src}   # rest Set - nodes with calculated distance
        while rsnwd:
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            u = self.minDistance (dist, rsnwd)
            #print (u, end = "  ")
            # remove minimum distance vertex from rest sets
            restSet.remove (u)
            rsnwd.remove (u)
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex is in rest set
            for v in self.edges [u]:
                if self.edists [(u, v)] > 0 and \
                    v in restSet and \
                    dist [v] > dist [u] + self.edists [(u, v)]:
                    rsnwd.add (v)
                    dist [v] = dist [u] + self.edists [(u, v)]
        dist.pop (src)
        return [-1 if x == maxsize else x for x in dist][1:]

# Complete the shortestReach function below.
def shortestReach (n, edges, edists, restSet, s):
    g = Graph (n, edges, edists)
    return g.dijkstra (s, restSet)

if __name__ == '__main__':
    fptr = open(environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        edges = defaultdict (set)
        edists = dict ()
        restSet = set ()  # all connected nodes to process
        for _ in range(m):
            u, v, d = map(int, stdin.readline().rstrip().split())
            if (u, v) in edists:
                if d < edists [(u, v)]:
                    edists [(u, v)] = d
                    edists [(v, u)] = d
            elif (v, u) in edists:
                if d < edists [(v, u)]:
                    edists [(u, v)] = d
                    edists [(v, u)] = d
            else:
                edists [(u, v)] = d
                edists [(v, u)] = d
                edges [u].add (v)
                edges [v].add (u)
                restSet.add (u)
                restSet.add (v)
        #print (restSet)
        s = int(input())
        result = shortestReach (n, edges, edists, restSet, s)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()

