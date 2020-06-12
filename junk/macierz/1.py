import numpy as np

n = np.zeros((10,10))
for i in range(0, 10,1):
    for j in range(0, 10,1):
        if(i==j):
            n[i][j] = i+1
print(n)
