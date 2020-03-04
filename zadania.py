import os
os.system('cls')#clear

print("Zadanie1: ")
calkowita=4
striing="Wyraz"
ulamek=12.53
print(calkowita)
print(striing)
print(ulamek)

print("Zadanie2: ")
a=5
b=4
print(f"1.Dodawanie: {a}+{b}={a+b}")
print(f"2.Odejmowanie: {a}-{b}={a-b}")
print(f"3.Mnożenie: {a}*{b}={a*b}")
print(f"4.Dzielenie: {a}/{b}={a/b}")
print(f"5.Dzielenie całkowite: {a}/{b}={a//b}")
print(f"6.Reszta z dzielenia: {a}%{b}={a%b}")
print(f"7.Potęgowanie: {a}%{b}={a**b} ")
print("Zadanie3: ")
print("operatory przedrostkowe")


print("Zadanie4: ")
from math import *
print("e^10= "+str(pow(e,10)))
print("|3.55|= "+str(abs(3.55))) #moze modf
print("|4.8|= "+str(abs(4.8)))

print("Zadanie5: ")
imie="WOJTEK"
nazwisko="PAKOCA"
print(imie.capitalize()+" "+nazwisko.capitalize())

print("Zadanie6: ")
tekst="tekst piosenki la la piosenka lo la la la la costam la la"
print("ilosc la w tekscie: "+str(tekst.count("la")))

print("Zadanie7: ")
samochod="czerwony"
print(samochod[1]+samochod[-1])

print("Zadanie8: ")
print(tekst.split())

print("Zadanie9: ")
zmienna_1="wyraz"
zmienna_2="15.2"
zmienna_3=0xDA5             
print("Zmienne: %(z1)s, %(z2)s, %(z3)s" %{"z1":zmienna_1,"z2":zmienna_2,"z3":zmienna_3}) #wszystko jako string

print("Zadanie10: ")
filmy= ["Skazani na Shawshank","Nietykalni","Zielona mila","Ojciec chrzestny","Dwunastu gniewnych ludzi","Forrest Gump","Joker"]
filmy.sort()
print(filmy)
