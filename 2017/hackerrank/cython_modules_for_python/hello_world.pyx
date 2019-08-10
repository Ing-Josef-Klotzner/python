#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
To use this to build your Cython file use the commandline options:
it must be installed (if not, use:)
sudo apt install cython3
sudo apt install python3-distutils

$ python3 setup.py build_ext --inplace
or
$ ./setup.py build_ext --inplace

the setup.py file:

#!/usr/bin/python3
# -*- coding: utf-8 -*-
from distutils.core import setup
from Cython.Build import cythonize
from sys import argv, stdin

print ("enter filename to process: ")
filename = stdin.readline ().strip ()
if len (argv) < 2 or filename == "":
    print ("usage: ./setup.py build_ext --inplace")
else:
    setup (
        ext_modules = cythonize (filename)
    )
"""
print ("hello world - this is imported cython module")
