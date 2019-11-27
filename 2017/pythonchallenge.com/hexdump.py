#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function
"""
Created on Wed Jul 26 19:55:51 2017

@author: josef
"""

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Specify a file')
    parser.add_argument('-s', '--screen', help='Print output to Terminal')
    
    args = parser.parse_args()
    
    if args.file:
        offset = 0
        with open(args.file, 'rb') as infile:
            with open(args.file+'.dump', 'w') as outfile:
                while True:
                    chunk = infile.read(16)
                    if len(chunk) == 0:
                        break
                    text = str(chunk)
                    text = ''.join([i if ord(i) < 128 and ord(i) > 31 else '.' for i in text])
                    output = '{:#08x}'.format(offset) + ': '
                    output += ' '.join('{:02X}'.format(ord(c)) for c in chunk[:8])
                    if len(chunk) > 8:                    
                        output += ' | '
                        output += ' '.join('{:02X}'.format(ord(c)) for c in chunk[8:])
                        output += ' '
                    else:
                        output += '   '
                    if len(chunk) % 16 != 0:
                        output += '   '*(16-len(chunk)) + text
                    else:
                        output += text
                    if args.screen:
                        print (output)
                    outfile.write(output + '\n')
                    offset += 16
    else:
        print (parser.usage)

if __name__ == '__main__':
    main()