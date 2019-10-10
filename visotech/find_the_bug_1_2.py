#!/usr/bin/python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

__author__      = "Ing. Josef Klotzner"
__version__     = "1.2"
__maintainer__  = "Ing. Josef Klotzner"
__status__      = "Draft"
__email__       = "josef.klotzner@gmail.com"
__date__        = "20190809"

from sys import version_info
if version_info.major == 3:
    pass
elif version_info.major == 2:
    input = raw_input
else:
    print ("Unknown python version - input function not safe")
from sys import argv, exit
"""
usage: find_the_bug.py bug_file landscape_file

This program collects a bug "shape" from an ascii text file "bug_file"
and counts and prints the number of occurances of this bug in an ascii file
"landscape_file"
This is more simple solution compared to V1.1, which has because of simplicity higher runtime. But simplicity does more insure correctness of solution related to more complex test data.
"""

# function to show bug or landscape (if not too big)
def show (block):
    for i, string in enumerate (block):
        print (i, string)

# scan through bug from top to bottom and left to right relative to
# landscape and check if each character is bugs character
# if yes return True, otherwise return False
# if during scan landscape dimension limits reached, return False
def is_bug (landscape, l_height, l_len, line, column, bug):
    for bug_line, bug_string in enumerate (bug):
        if line + bug_line >= l_height: return False
        for bug_col, char in enumerate (bug_string):
#            print (line, bug_line, l_height, column, bug_col, l_len)
            if char == " ": continue
            if column + bug_col >= l_len: return False
            if char != landscape [line + bug_line] [column + bug_col]:
                return False
    return True

def count_bugs (bug, landscape, l_height, l_len):
    """ scan through landscape
     reference to a bug to its upper left position.
     bug identification: whenever a first bug stringcharacter is found in
     a landscape string, check with is_bug function, if it is a bug by 
     scanning through all buglines, so it is no O (n) solution any more.
     if a bug is found, add bug counter
    """
    bug_counter = 0
    for line, string in enumerate (landscape):
        for column, char in enumerate (string):
            if char == bug [0] [0]: 
                if is_bug (landscape, l_height, l_len, line, column, bug):
                    bug_counter += 1
    return bug_counter            

def main ():
    # ensure correct input leading the user
    # if input format is incorrect, inform user how to do it and exit
    if len (argv) < 3:
        print ("usage: " + argv [0] + " bug_file landscape_file")
        print ("bug_file and landscape_file must be in same")
        print ("directory as program or enter /full_path_to/filename")
        exit ()
    
    bugfile = open (argv [1], 'r')
    # convert bug from file into list of strings
    bug = []
    # maximum length of bug
    b_len_max = 0
    for string in bugfile:
        bug.append (string [ : -1])  # remove \n
        b_len_max = max (len (string) - 1, b_len_max)
    # height of bug
    b_height = len (bug)
#    show (bug)
    bugfile.close ()
    
    landscapefile = open (argv [2], 'r')
    # convert landscape from file into list of strings
    landscape = []
    string = next (landscapefile)
    landscape.append (string [ : -1])
    # length of stringline in landscape (-1 because of \n (new line))
    l_len = len (string) - 1
    for string in landscapefile:
        if string [ : -1] != "":
            landscape.append (string [ : -1])
    # height of landscape
    l_height = len (landscape)
#    show (landscape)
    landscapefile.close ()

    if l_len >= b_len_max and l_height >= b_height:
        bug_counter = count_bugs (bug, landscape, l_height, l_len)
        # remove comment if pretty user output is wanted:
        #print ("number of bugs found: ", end = "")
        print (bug_counter)
    else: print (0)

if __name__ == '__main__':
    main ()
