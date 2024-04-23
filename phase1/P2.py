"""
The Gibbs phenomenon is the name given to the oscillations observed in the fourier series of a periodic function newar to a step discontinuity. For example, the square wave defined by f(x) = 1 for 0<x<1 and f(x) = -1 for 1<x<2 and repeating outside the range(0, 2) has the Fourier series expansion:
f(x) = 4/pi * ∑n=1, 3, 5,... 1/n*sin(npix)
Plot f(x) and its Fourier series expansion truncated at 20 terms on the same axes, (a) for 0<x<4 and (b) zoomed in on a region exhibition the Gibbs phenomenon.
"""

# needed imports
import math
import matplotlib.pyplot as plt
import numpy as np

# function to get expansion
def fourier(x):
    y = 4 / math.pi
    total = 0
    count = 0
    for i in range(1, 41, 2): # goes 20 times at the right inteorvals
        total += (1/i) * math.sin(i * math.pi * x) # formula in summation
        count += 1
    return y * total # final number returned

# a
xlist = np.linspace(0, 4, 80) # list of 20 numbers evenly space from 0 to 4 inclusive
plt.plot(xlist, [fourier(i) for i in xlist]) # use xs and find the ys
plt.xlabel('X') # labels
plt.ylabel('Fourier Expansion')
plt.title('Gibbs Phenomenon')
plt.show() # show the graph


# b
xlist2 = np.linspace(.8, 1.2, 20)
plt.plot(xlist2, [fourier(i) for i in xlist2])
plt.xlabel('X')
plt.ylabel('Fourier Expansion')
plt.title('Gibbs Phenomenon')
plt.show()
