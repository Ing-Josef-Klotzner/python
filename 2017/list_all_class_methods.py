#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function
"""
Created on Mon Jul 17 17:48:35 2017

@author: josef
"""
import inspect
from sys import argv
import importlib

if len(argv) == 1:
	print ("Verwendung: "+argv[0]+" 'Klassenobjekt von welchem die Methoden aufgelistet \
 werden sollen'")
	print ("Es werden per default Methoden des Klassenobjektes print aufgelistet")
	argv.append('print')
object = argv[1]

try:
    importlib.import_module(object)
except ImportError:
    print ("import von "+object+" ging schief")
#print ([method for method in dir(object) if callable(getattr(object, method))])
#print (dir(object))

help (object)
"""
Introducing IPython
You don’t need to know anything beyond Python to start using IPython – just type commands as you would at the standard Python prompt. But IPython can do much more than the standard prompt. Some key features are described here. For more information, check the tips page, or look at examples in the IPython cookbook.

If you’ve never used Python before, you might want to look at the official tutorial or an alternative, Dive into Python.

The four most helpful commands
The four most helpful commands, as well as their brief description, is shown to you in a banner, every time you start IPython:

command	description
?	Introduction and overview of IPython’s features.
%quickref	Quick reference.
help	Python’s own help system.
object?	Details about ‘object’, use ‘object??’ for extra details.
Tab completion
Tab completion, especially for attributes, is a convenient way to explore the structure of any object you’re dealing with. Simply type object_name.<TAB> to view the object’s attributes (see the readline section for more). Besides Python objects and keywords, tab completion also works on file and directory names.

Exploring your objects
Typing object_name? will print all sorts of details about any object, including docstrings, function definition lines (for call arguments) and constructor details for classes. To get specific information on an object, you can use the magic commands %pdoc, %pdef, %psource and %pfile

Magic functions
IPython has a set of predefined ‘magic functions’ that you can call with a command line style syntax. There are two kinds of magics, line-oriented and cell-oriented. Line magics are prefixed with the % character and work much like OS command-line calls: they get as an argument the rest of the line, where arguments are passed without parentheses or quotes. Cell magics are prefixed with a double %%, and they are functions that get as an argument not only the rest of the line, but also the lines below it in a separate argument.

The following examples show how to call the builtin %timeit magic, both in line and cell mode:

In [1]: %timeit range(1000)
100000 loops, best of 3: 7.76 us per loop

In [2]: %%timeit x = range(10000)
   ...: max(x)
   ...:
1000 loops, best of 3: 223 us per loop
The builtin magics include:

Functions that work with code: %run, %edit, %save, %macro, %recall, etc.
Functions which affect the shell: %colors, %xmode, %autoindent, %automagic, etc.
Other functions such as %reset, %timeit, %%writefile, %load, or %paste.
You can always call them using the % prefix, and if you’re calling a line magic on a line by itself, you can omit even that:

run thescript.py
"""