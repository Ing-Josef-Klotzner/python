#! /usr/bin/env python
# zip_2.py  --  created by Ing. Josef Klotzner
import zipfile
f = "channel.zip"
z = zipfile.ZipFile(f)

name = '90052.txt'
while 1:
    print z.getinfo(name).comment,
    name = z.read(name).split()[-1] + '.txt'
