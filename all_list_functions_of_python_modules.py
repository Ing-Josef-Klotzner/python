#!/usr/bin/python
import re
from sys import argv

def dummy():
    return

if __name__ == "__main__":
    if len(argv) == 1:
        print
        print ("usage: "+argv[0]+" 'python module to inspect'")
        print ("default is inspecting itself")
        argv.append(argv[0])

    pattern = re.compile("def (.*)\(*\):")
    print
    print "functions of python module: "+argv[1]
    for i, line in enumerate(open(argv[1])):
        for match in re.finditer(pattern, line):
            print '  %s: %s' % (i+1, match.groups()[0]+")")
    print
