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


funkcjazad4(2, 10)


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

print("Zadanie 6: wykreślanka ")
# Stwórz skrypt który na wyjściu wyświetli macierz numpy(tablica wielowymiarowa) w postaci wykreślanki,
# gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie.
# Jedno z tych słów powinno być wypisane od prawej do lewej.


def funkcjazad6(n):
    slowa = ['marcin', 'uihqke', 'csłqwe', 'hweawe', 'akzcat']
    s = [[], [], [], [], []]
    # marcin 1 linjka, miła po ukosie, mucha 1 kolumna, taczka od tylu ostatni wiersz
    for i in range(0, 5, 1):
        s[i] = np.array(list(slowa[i]))
        s[i] = np.fromiter(slowa[i], dtype='U1')
        print(s[i])


funkcjazad6(6)
print("Zadanie 7: ")
# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# [[2 4 6]
#  [4 2 4]
#  [6 4 2]]
# funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n
# i umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.


def funkcjazad7(n):
    przek = [2 for x in range(n)]
    A = np.diag(przek)
    for a in range(0, n):
        for b in range(0, n):
            for c in range(1, n+1):
                if(a == b+c or b == a+c):
                    A[a, b] = 2*(c+1)

    print(f"Macierz:\n{A}")


funkcjazad7(15)


print("Zadanie 8: ")
# jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr ‘kierunek’,
# parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
# funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że ilość wierszy lub kolumn, w zależności od kierunku podziału, nie pozwala na operację)


def funkcjazad8(n):
    pass


funkcjazad8(1)


print("Zadanie 9: ")
# Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5,
# która będzie zawierała kolejne wartości ciągu Fibonacciego.


def funkcjazad9(n):
    a = [1, 1]
    for i in range(n*n-2):
        a.append(a[i] + a[(i + 1)])
    fi = np.asarray(a)
    b = np.reshape(fi, (n, n))
    print(b)


funkcjazad9(5)
