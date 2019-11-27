#! /usr/bin/env python2
# len_.py  --  created by Ing. Josef Klotzner
# a = [1, 11, 21, 1211, 111221, (?) 21112211,
a = [1,11,21,1211,111221]
# len(a[30]) = ?
# len(str(a[30]))   ....   to be able to use len on integer
import re
def describe(s):
    return "".join([str(len(m.group(0))) + m.group(1)
                    for m in re.finditer(r"(\d)\1*", s)])
s = "1"
for dummy in range(30):
    s = describe(s)
    print len(s),
    if len(s) < 103:
        print s
    else:
        print
print len(s)  # prints 5808
"""
count = 0
s = "1"
a = [s]
while count < 31:
   j = 0
   news = ""
   while j < len(s):
       i = j
       while j < len(s) and s[i] == s[j]:
           j += 1
       news += str(j-i) + s[i]
   a += [news]
   s = news
   count += 1
print len(a[30])
"""
