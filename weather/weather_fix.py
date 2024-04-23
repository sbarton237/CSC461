import numpy as np
import matplotlib.pyplot as plt

dtype1 = np.dtype([('temp', 'f8'), ('pressure', 'f8')])
weather = np.genfromtxt("Weather\\weather-raw.csv", dtype=dtype1, delimiter=",", usecols=(1,4),filling_values=-9999)

weather['temp'] = weather['temp']/10

validTemp = weather['temp'] > -999.9
validPressure = weather['pressure'] > -9999

corr = np.corrcoef(weather['temp'][validTemp & validPressure], weather['pressure'][validTemp & validPressure])

plt.scatter(weather['pressure'][validTemp & validPressure], weather['temp'][validTemp & validPressure], marker=".", alpha=.01)
plt.ylabel("Temperature (C)")
plt.xlabel("Pressure (mmHg)")

plt.show()

print(corr)
