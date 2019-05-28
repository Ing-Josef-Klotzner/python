#! /usr/bin/env python
# pi_ckle.py  --  created by Ing. Josef Klotzner
import pickle
import urllib

handle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(handle)
handle.close()
 
for elt in data:
    print "".join([e[1] * e[0] for e in elt])

"""
import urllib
def get_nothing(next_nothing):
    contents = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={next_nothing}".format(next_nothing=next_nothing)).read()
    new_nothing = re.search(r'the next nothing is (\d+)', contents)
    return new_nothing.group(1)
nothing_collection = []
nothing_collection.append('12345')
for a in xrange(399):
    last_nothing = nothing_collection[a]
    new_nothing = get_nothing(last_nothing).group()
    nothing_collection.append(new_nothing)
print nothing_collection
"""
