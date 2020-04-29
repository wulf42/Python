import pandas as pd
import numpy as np
import xlrd
import openpyxl
import os
os.system('cls')


# zadanie 1
print("Zadanie 1")
xlsx = pd.ExcelFile(
    'D:\programowanie\wizualizacja danych\Lekcje\Lekcja7\imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')
print(df)


# zadanie 2
print("Zadanie 2")
# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
print(df[df['Liczba'] > 1000])
# tylko rekordy gdzie nadane imię jest takie jak Twoje
print(df[df['Imie'] == 'WOJTEK'])
# sumę wszystkich urodzonych dzieci w całym danym okresie
print(df.agg({'Liczba': ['sum']}))
# sumę dzieci urodzonych w latach 2000-2005
print(df[df['Rok'] <= 2005].agg({'Liczba': [sum]}))
# sumę urodzonych chłopców i dziewczynek
print(df[df['Plec'] == "M"].agg({'Liczba': [sum]}))
print(df[df['Plec'] == "K"].agg({'Liczba': [sum]}))
# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)



print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
# # pierwsze 2 wiersze każdej grupy
print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth([0, 1]))
new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
for index, group in enumerate(new_df, start=1):
    print(f"{index} {group[0]}")
    print(f" {group[1].iloc[0]['Imie']}", end='')
    print(f" {group[1].iloc[0]['Liczba']}")









# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie
print("y")
