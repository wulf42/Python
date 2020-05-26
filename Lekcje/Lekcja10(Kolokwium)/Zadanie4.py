import os
os.system('cls')

# 1 Pakoca Wojciech zestaw_20200513_ISI2_1

def zadanie4(n):
    print([2 * (x ** 2) for x in range(1, n + 1, 1)])


zadanie4(int(input("Podaj n: ")))