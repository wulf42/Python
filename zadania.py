import os
os.system('CLS')#clear
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

print(f"e^10={pow(e,10)}") 
print(f"|3.55|= {abs(3.55)}") #moze modfs
print(f"|4.8|= {abs(4.8)}") #moze modfs

print("Zadanie5: ")
imie="WOJTEK"
nazwisko="PAKOCA"
print(imie.capitalize(), nazwisko.capitalize())

print("Zadanie6: ")
tekst="tekst piosenki la la piosenka lo la la la la costam la la"
print(f"ilosc la w tekscie: {tekst.count('la')}")

print("Zadanie7: ")
samochod="czerwony"
print(samochod[1]+samochod[-1])

print("Zadanie8: ")
print(tekst.split())

print("Zadanie9: ")
zmienna_1="wyraz"
zmienna_2="15.2"
zmienna_3=0xDA5             
print(f"{zmienna_1}, {zmienna_2}, {zmienna_3}") 

print("Zadanie10: ")
filmy= ["Skazani na Shawshank","Nietykalni","Zielona mila","Ojciec chrzestny","Dwunastu gniewnych ludzi","Forrest Gump","Joker"]
filmy.sort()
print(filmy)

print("Zadanie11: ")
pi=["0","\u03A0/6","\u03A0/4","\u03A0/3","\u03A0/2","\u03A0"]
stopnie=["0°","30°","45°","60°","90°","180°"]
sinus=[0,1/2,"√2/2","√3/2",1,0]
print(pi,stopnie,sinus)

