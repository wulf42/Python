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


def funkcjazad3(n):
    A = np.arange(1, n*n+1)
    B = A.reshape(n, n)
    print(B)


funkcjazad3(4)


print("Zadanie 4: ")
# napisz funkcję, która będzie przyjmowała 2 parametry:
# liczbę, która będzie podstawą operacji potęgowania oraz ilość kolejnych potęg do wygenerowania.
# Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg podanej liczby,
# np. generuj(2,4) -> [2 4 8 16]


def funkcjazad4(n, x):
    A = np.logspace(1, x, num=x, base=n, dtype=int)
    print(A)


funkcjazad4(5, 5)


print("Zadanie 5: ")
# Napisz funkcję, która:
# na wejściu przyjmuje jeden parametr określający długość wektora,
# na podstawie parametru generuje wektor, ale w kolejności odwróconej (czyli np. dla n=3 =>[3 2 1])
# generuje macierz diagonalną z w/w wektorem jako przekątną


def funkcjazad5(n):
    A = np.arange(1, n+1)
    B = sorted(A, reverse=True)
    print(f"Wektor:\n{B}")
    B_diag = np.diag(B)
    print(f"Macierz:\n{B_diag}")


funkcjazad5(4)

print("Zadanie 6: ")
# Stwórz skrypt który na wyjściu wyświetli macierz numpy(tablica wielowymiarowa) w postaci wykreślanki,
# gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie.
# Jedno z tych słów powinno być wypisane od prawej do lewej.


def funkcjazad6(n):
    pass


funkcjazad6(4)
