#! /usr/bin/env python2
# balloons.py  --  created by Ing. Josef Klotzner
#http://www.pythonchallenge.com/pc/return/romance.html
import codecs,re
deltas = open('delta.txt').read()
lines = deltas.split('\n')
pairs = [(l[:53], l[56:]) for l in lines]
columns = ['\n'.join([p[i] for p in pairs]) for i in range(2)]
import codecs
def unhex(s): return codecs.getdecoder('hex')(re.sub('[^0-9a-fA-F]', '', s))[0]

for i in range(2): open('delta%d.png' % i,'wb').write(unhex(columns[i]))
import difflib
column_diffs = list(difflib.Differ().compare(columns[0].splitlines(),
                                             columns[1].splitlines()))
pngs = [''.join(filter(lambda l: l[0] == d, column_diffs)) for d in " -+"]
for i in range(len(pngs)): open('delta%d.png' % (i + 2), 'wb').write(unhex(pngs[i]))
