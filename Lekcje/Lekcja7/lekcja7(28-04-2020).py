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
print("a:")
print(df[df['Liczba'] > 1000])
# tylko rekordy gdzie nadane imię jest takie jak Twoje
print("b:")
print(df[df['Imie'] == 'WOJTEK'])
# sumę wszystkich urodzonych dzieci w całym danym okresie
print("c:")
print(df.agg({'Liczba': ['sum']}))
# sumę dzieci urodzonych w latach 2000-2005
print("d:")
print(df[df['Rok'] <= 2005].agg({'Liczba': [sum]}))
# sumę urodzonych chłopców i dziewczynek
print("e:")
print(df[df['Plec'] == "M"].agg({'Liczba': [sum]}))
print(df[df['Plec'] == "K"].agg({'Liczba': [sum]}))
# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)
print("f:")
print(df.sort_values('Liczba', ascending=False).groupby(
    ['Rok', 'Plec']).nth(0))
# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie
print("g:")
print(df.groupby(['Plec', 'Imie']).agg({'Liczba': ['sum']}).sort_values(
    ('Liczba', 'sum'), ascending=False).iloc[[0, 1]])

# zadanie 3
print("Zadanie 3")
xlsx = pd.ExcelFile(
    'D:\programowanie\wizualizacja danych\Lekcje\Lekcja7\zamowienia.xlsx')
df = pd.read_excel(xlsx, 'zamowienia')
# listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
print("a:", end="   ")
print(df['Sprzedawca'].unique())

# 5 najwyższych wartości zamówień
print("b:")
print(df['Utarg'].nlargest(5))

# ilość zamówień złożonych przez każdego sprzedawcę
print("c:")
print(df.groupby('Sprzedawca')['Sprzedawca'].count())
# sumę zamówień dla każdego kraju
print("d:")
print(df.groupby(['Kraj']).agg({'Utarg': ['sum']}))
# sumę zamówień dla roku 2005, dla sprzedawców z Polski
print("e:")
print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '01-01-2005')
         & (df['Data zamowienia'] <= '31-12-2005')].agg({'Utarg': ['sum']}))
# średnią kwotę zamówienia w 2004 roku
print("\nf:", end=" ")
print(df['Utarg'][(df['Data zamowienia'] >= '01-01-2004')
                  & (df['Data zamowienia'] <= '31-12-2004')].mean())
# zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
df2004=df[(df['Data zamowienia'] >= '01-01-2004') & (df['Data zamowienia'] <= '31-12-2004')]
df2004.to_csv('D:\programowanie\wizualizacja danych\Lekcje\Lekcja7\zamówienia_2004.csv')
df2005=df[(df['Data zamowienia'] >= '01-01-2005') & (df['Data zamowienia'] <= '31-12-2005')]
df2005.to_csv('D:\programowanie\wizualizacja danych\Lekcje\Lekcja7\zamówienia_2005.csv')

