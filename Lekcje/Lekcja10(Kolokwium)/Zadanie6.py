import os
import random
os.system('cls')

# 1 Pakoca Wojciech zestaw_20200513_ISI2_1
lista = []
temp = []
for i in range(10):
    for j in range(10):
        temp.append(random.randint(1, 10))
    lista.append(temp)
    temp = []
print("Macierz:")
for i in range(10):
    print(lista[i])
suma1 = 0
suma2 = 0
for n in range(0, 10, 1):
    suma1 += lista[n][n]
for n in range(0, 10, 1):
    suma2 += lista[n][n-9]
print(f"Suma przekątnej 1 :{suma1}")
print(f"Suma przekątnej 2 :{suma2}")
