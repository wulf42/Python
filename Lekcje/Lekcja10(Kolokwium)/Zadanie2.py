import os
os.system('cls')

# 1 Pakoca Wojciech zestaw_20200513_ISI2_1

def licznik(tekst):
    dlugosc = len(tekst)
    spacje = tekst.count(" ")
    przecinki = tekst.count(",")
    kropki = tekst.count(".")
    ilosc_znakow = dlugosc-spacje-przecinki-kropki
    print(
        f"Ilość znaków nie uwzględniając przecinków spacji i kropek: {ilosc_znakow}")


a = "Przykładowy tekst w którym są spacje, przecinki. Kropki też się znajdą."
licznik(a)