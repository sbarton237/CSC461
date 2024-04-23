import numpy as np

arr = np.loadtxt("Phase 2\student-data.txt", dtype=str)
a = np.empty(0)
for line in arr:
    if line[1] == "F":
        if line[-1] != "-":
            a = np.append(a, float(line[-1]))
print(round(a.mean(), 2))

arr = np.loadtxt("Phase 2\Iris.csv", delimiter=",", dtype=str)
se = np.empty(0)
ve = np.empty(0)
vi = np.empty(0)
for line in arr:
    if line[5] == "Iris-setosa":
        se = np.append(se, float(line[1]))
    elif line[5] == "Iris-versicolor":
        ve = np.append(ve, float(line[1]))
    elif line[5] == "Iris-virginica":
        vi = np.append(vi, float(line[1]))
avs = np.array([se.mean(), ve.mean(), vi.mean()])
print(round(avs.mean(), 2))
