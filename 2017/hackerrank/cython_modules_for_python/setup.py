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
