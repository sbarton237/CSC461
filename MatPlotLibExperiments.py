import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 10)

plt.plot(x, np.sin(x), label=('sin(x)'), linestyle='', marker='^', color='blue')
plt.plot(x, np.cos(x), label=('cos(x)'), linestyle='', marker='^', color='red')

plt.ylabel('f(x)')
plt.xlabel('x')

plt.legend(loc="lower left")
plt.show() 