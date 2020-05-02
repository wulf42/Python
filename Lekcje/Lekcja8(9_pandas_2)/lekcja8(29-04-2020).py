import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
import os
os.system('cls')
# Zadanie 1 Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.
xlsx = pd.ExcelFile(
    'D:\programowanie\wizualizacja danych\Lekcje\Lekcja8(9_pandas_2)\imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')
a = df.groupby('Rok').agg({'Liczba': ['sum']})
wykres = a.plot(marker='+')
wykres.set_ylabel('Ilość')

wykres.legend().remove()
plt.title('Ilość urodzonych dzieci dla każdego roku')
plt.show()

# Zadanie 2 Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.
b = df.groupby('Plec').agg({'Liczba': ['sum']})
wykres = b.plot.bar()
plt.title('Ilość urodzonych dzieci ze względu na płeć')
wykres.legend().remove()
wykres.set_ylabel('Ilość [Mln]')
plt.show()

# Zadanie 3 Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.
c = df.groupby(['Rok', 'Plec']).agg({'Liczba': ['sum']}).sort_values(
    ('Rok'), ascending=False).head(10)
wykres = c.plot.pie(subplots=True, figsize=(10, 10), fontsize=12)
plt.title(
    'Ilość urodzonych dzieci w ostatnich 5 latach ze względu na płeć i rok urodzenia')
plt.show()
# Zadanie 4 Z repozytorium UCI (httpa://rchive.ics.uci.edu/ml/index.php) pobierz dataset Iris i za pomocą wykresu punktowego (scattered) wyświetl wartość 2 wybranych cech tego datasetu. Dla każdego rodzaju kwiatu użyj innego koloru na wykresie. Przykład można znaleźć w galerii wykresów biblioteki matplotlib - link w materiałach matplotlib.



# Zadanie 5 Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór danych zamówienia.csv).
xlsx = pd.ExcelFile(
    'D:\programowanie\wizualizacja danych\Lekcje\Lekcja7(8_pandas_1)\zamowienia.xlsx')
df = pd.read_excel(xlsx, 'zamowienia')
e = df.groupby('Sprzedawca')['Sprzedawca'].count()
wykres = e.plot.bar()
plt.title('Ilość zamówień złożonych przez poszczególnych sprzedawców')
wykres.legend().remove()
wykres.set_ylabel('Ilość')
plt.show()
