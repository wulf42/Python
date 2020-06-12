import numpy as np
import os

os.system("cls")
n = np.zeros((10, 10))
for i in range(0, 10, 1):
    for j in range(0, 10, 1):
        if (i == j):
            n[i][j] = 10 - i
print(n)


print("zmiana bardzo ważna")
