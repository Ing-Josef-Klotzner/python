#  heapq
# -*- coding: iso-8859-15 -*-
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print 'List original', data
print "heapify sortiert die Liste:"
heapify(data)                      # rearrange the list into heap order
print data
print "heappush fuegt -5 zur Liste: "
heappush(data, -5)                 # add a new entry
print data
print 'Anwendung von heappop:'
print [heappop(data) for i in range(3)]  # fetch the three smallest entries
print 'List heapified', data
print "Achtung: nach heappop sind diese Werte nicht mehr in der Liste!"