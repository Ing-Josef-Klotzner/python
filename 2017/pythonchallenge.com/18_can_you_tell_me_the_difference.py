#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import gzip, difflib
"""
18 can you tell me the differnce?
"""
site = "http://www.pythonchallenge.com/pc/return/"
opt = "balloons.html"

"""
18_can_you_tell_me_the_difference_balloons.jpg
when trying 'brightness: new hint -> http://www.pythonchallenge.com/pc/return/brightness.html
<!-- maybe consider deltas.gz -->'
--> http://www.pythonchallenge.com/pc/return/deltas.gz
--> download 
file holding 
89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00   89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00\n
02 8a 00 00 00 c8 08 02 00 00 00 e0 19 57 95 00 00 00   02 8a 00 00 00 c8 08 02 00 00 00 e0 19 57 95 00 00 00\n
09 70 48 59 73 00 00 0b 13 00 00 0b 13 01 00 9a 9c 18   09 70 48 59 73 00 00 0b 13 00 00 0b 13 01 00 9a 9c 18\n
89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00
which differ later on in file
... so it is supposed to work out difference

- appear in left, not in right
+ appear in right, not in left
  appear in both
"""
test = "\
89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00   89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00\n\
02 8a 00 00 00 c8 08 02 00 00 00 e0 19 57 95 00 00 00   02 8a 00 00 00 c8 08 02 00 00 00 e0 19 57 95 00 00 00\n\
09 70 48 59 73 00 00 0b 13 00 00 0b 13 01 00 9a 9c 18   09 70 48 59 73 00 00 0b 13 00 00 0b 13 01 00 9a 9c 18\n\
33 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 11"



with gzip.open("18_deltas.gz") as content:
    cont = content.read()

#lines_list = (test.split("\n"))
lines_list = (cont.split("\n"))
left = [(x[:53]) for x in lines_list]
#left = unique(left)

right = [x[56:109] for x in lines_list]
#right = unique(right)
print(len(left))
print(len(right))

compare = difflib.Differ().compare(left, right)
print(compare)

# solution 1: using difflib

f = open("18_f.png", "wb")
f1 = open("18_f1.png", "wb")
f2 = open("18_f2.png", "wb")
c = 0
for line in compare:
    c += 1
#    print(c, line)
    bs = filter(lambda x: x != " ", line[2:]).decode("hex")
    if line[0] == '+':
        f1.write(bs)
    elif line[0] == '-':
        f2.write(bs)
    else:
        f.write(bs)

f.close()
f1.close()
f2.close()

# solution 2: create own diff

# first lines of left and right are showing PNG, so are pictures:
outleft, outright, outcombi, l, r = "", "", "", 0, 0
with open('18_left.png', 'w') as leftf:  #(only additional lines not in right)
    with open('18_right.png', 'w') as rightf:  # (only additional lines not in left)
        with open('18_combi.png', 'w') as combif:

            while l < len(left):
                if left[l] == right[r]:
                    outcombi += filter(lambda x: x != " ",left[l]).decode("hex")
                elif left[l] not in right[r:] or right[r] in left[l:]:    
                    outleft += filter(lambda x: x != " ",left[l]).decode("hex")
                    r -= 1
                elif right[r] not in left[l:] or left[l] in right[r]:
                    outright += filter(lambda x: x != " ",right[r]).decode("hex")
                    l -= 1
                l += 1
                r += 1
            leftf.write(outleft)
            rightf.write(outright)
            combif.write(outcombi)

print(l, r)

answer_to_find = "to see in pictures: '../hex/bin.html' 'butter' 'fly'"
#print("answer to find is: ", answer_to_find)
#opt = "".join(x for x in lower(answer_to_find) if x in letters)
#print(" new site: http://www.pythonchallenge.com/pc/return/" + opt + ".html")
print("answer to find:", answer_to_find)
##webbrowser.open(site + answer_to_find)


