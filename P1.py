"""
The expansion of the spherical ball of fire generated in an explosion may be analyzed to deduce the initial energy, E, released by a nuclear weapon. The Biritish physicist Geoffrey Taylor used dimensional analysis to demonstrate that the radius of this sphere, R(t) should be related to E, the air density, pair, and time, t, through R(t) = CE^1/5 * pair^-1/5 * t^2/5, where, using model-shock wave problems, Tayler estimated the dimensionless constant C≈1. Using the data obtained from declassified timed images of the first New Mexico atomic explosion, Taylor confirmed this law and produced an estimate of the (then unknown) value of E. Use a log-log plot to fit the data in new-mexico-blast-data.txt to the model and confirm the time-dependence of R. Taking pair = 1.25kgm^-3 deduce E and express its value in Joules and in 'kilotons of TNT' where the explosive energy released by 1 ton of TNT is arbitrarily defined to be 4.184 * 10^9 J.
"""

import numpy as np
import matplotlib.pyplot as plt

arr = np.loadtxt('Phase 2\\blast-data.txt', skiprows=1)
c = 1
pair = 1.25

y = np.array(arr[0])
x = np.empty(0)
for el in arr[1]:
    x = np.append(x, c * (pair ** -1/5) * (el ** 2/5))

plt.plot(x ** 1/5, y)
plt.show()