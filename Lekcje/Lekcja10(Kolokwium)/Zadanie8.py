import os
os.system('cls')

# 1 Pakoca Wojciech zestaw_20200513_ISI2_1


def zad8(sciezka):
    lista = []
    with open(sciezka) as plik:
        for linia in plik:
            imie, punkty = linia.strip().split()
            lista.append({'imie': imie, 'punkty': punkty})
    print(lista)

zad8("D:\programowanie\wizualizacja danych\Lekcje\Lekcja10(Kolokwium)\Zadanie8.txt")
