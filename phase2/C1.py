import numpy as np
import matplotlib.pyplot as plt

arr = np.loadtxt("Phase 2\\amine_bp.csv", delimiter=",", skiprows=1)

plt.plot([arr[i][0] for i in range(len(arr))], [arr[i][1] for i in range(len(arr))], marker="o", color="red", label=("primary"), linestyle='')
plt.plot([arr[i][0] for i in range(len(arr))], [arr[i][2] for i in range(len(arr))], marker="^", color="green", label=("secondary"), linestyle='')
plt.plot([arr[i][0] for i in range(len(arr))], [arr[i][3] for i in range(len(arr))], marker="d", color="blue", label=("tertiary"), linestyle='')
plt.legend()
plt.show()
