import numpy as np
import matplotlib.pyplot as plt

arr = np.loadtxt("Phase 2\\amine_bp.csv", delimiter=",", skiprows=1)
#https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html

plt.plot([arr[i][0] for i in range(len(arr))], [arr[i][1] for i in range(len(arr))], marker="o", color="red", label=("primary"), linestyle='')
plt.plot([arr[i][0] for i in range(len(arr))], [arr[i][2] for i in range(len(arr))], marker="^", color="green", label=("secondary"), linestyle='')
plt.plot([arr[i][0] for i in range(len(arr))], [arr[i][3] for i in range(len(arr))], marker="d", color="blue", label=("tertiary"), linestyle='')
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

plt.legend()
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html

plt.show()
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html
