import os
os.system('cls')

# 1 Pakoca Wojciech zestaw_20200513_ISI2_1


def licznik(sciezka):
    plik = open(sciezka)
    tekst = plik.read()
    pytajace = tekst.count("?")
    twierdzace = tekst.count(".")
    wykrzynikowe = tekst.count("!")
    ilosc_zdan = pytajace+twierdzace+wykrzynikowe
    print(f"Ilość zdań: {ilosc_zdan}")


licznik("D:\programowanie\wizualizacja danych\Lekcje\Lekcja10(Kolokwium)\zadanie1.txt")


