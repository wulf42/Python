import numpy as np
import os
os.system('cls')
# import numpy z indexem np.
print("Zadanie 1: ")
# Za pomocą funkcji arange stwórz tablicę Numpy składającą się 20 kolejnych wielokrotności liczby 2.
a = np.arange(1, 21, 1)
a = 2**a
print(a)
print("Zadanie 2: ")
# Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int64.
l2 = np.array([1.24, 6.12, 4.12, 8.12, 9.11, 11.93, 13.33])
print(l2.dtype)
l3 = l2.astype('int64')
print(l3.dtype)
print("Zadanie 3: ")
# Napisz funkcję, która będzie:
# przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1
# Istnieją sposoby na szybkie stworzenie bardziej rozbudowanych tablic/macierzy.

