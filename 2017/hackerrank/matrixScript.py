#!/usr/bin/python3

import re

n, m = map (int, input ().split ())
matrix = []
# symbols = "!@#$%&"
for _ in range (n):
    matrix_item = input ()
    matrix.append(matrix_item)
result = ""
for z in zip(*matrix):
    result += "".join(z)
#result = re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', result)
result = re.sub(r'(\w)(\W)+(\w)', r'\1 \3', result)
print (result)

"""
test input:

7 3                  
Tsi
h%x
i #
sM 
$a 
#t%
ir!

shall give output:

This is Matrix# %!

"""
