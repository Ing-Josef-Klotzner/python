#! /usr/bin/env python
# url_lib.py  --  created by Ing. Josef Klotzner

import re
import urllib
target=12345 
#start with target 12345 and then with half 8022 
#target = 8022
TARGET_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
while True:
    source = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(target)).read()
    found = re.findall('[0-9]+', source)
    if found:
        target = found[-1]
        print target
    else:
        print source
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
