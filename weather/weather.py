import numpy as np

arr = np.genfromtxt("Weather\\weather-raw.csv", delimiter=",", filling_values=-1000)

temp = arr[:,1]
pressure = arr[:,4]

temp /= 10

print(np.corrcoef(temp, pressure))
