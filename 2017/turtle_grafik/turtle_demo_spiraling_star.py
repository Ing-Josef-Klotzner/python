#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Mon Sep 25 23:16:54 2017

@author: josef
"""

from turtle import fd, right, done, bgcolor, pencolor

bgcolor("black")
pencolor("yellow")
for _ in range(65):
    fd(_ * 5)
    right(144)

done()


