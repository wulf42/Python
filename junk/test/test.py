import numpy as np

n = np.ones((30,10))  
for i in range(0, 30,1):  
    for j in range(1, 10,2):
        n[i][j] = 0
print(n)
print("test")



