#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Wertereihen erzeugen:
x = np.arange (start = 1, stop = 9, step = 0.1)
y = x ** 2 + x + 1 / x
# Funktion plotten:
plt.plot (x, y)
# Layout anpassen:
plt.axis ([0, 10, 0, 100])
plt.xlabel ("$x$")
plt.ylabel ("$y$")
plt.grid (True)
plt.text (3.5, 30, "$f(x)=x^2 + x + 1/x$")
plt.show()
