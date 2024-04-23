"""
The iterative weak acid approximation determines the hydrogen ion concentration, [H+], of an acid solution from the acid dissociation 
constant, Ka, and the acid concentration, c, by successive application of the formula starting with [H+]0 = 0. The iterations are 
continued until [H+] changes by less than some predetermined, small tolerance value. Use this method to determine the hydrogen ion 
concentration, and hence the pH (=-log10[H+]) of a c=0.01 M solution of acetic acid (Ka = 1.78 x 10-5).  Use the tolerance TOL = 1.e-10.
"""

from math import sqrt, log10

c = 0.01
ka = 1.78 * (10 ** -5)

prev = -1
h = 0
while h - prev > 10 ** -10:
    prev = h
    h = sqrt(ka * (c - prev))

ph = -log10(h)
print("Ph = " + str(ph))
