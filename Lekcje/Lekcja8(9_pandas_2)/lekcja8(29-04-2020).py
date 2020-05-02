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
# a = df.groupby('Rok').agg({'Liczba': ['sum']})
# wykres = a.plot(marker='+')
# wykres.set_ylabel('Ilość')
# wykres.set_xlabel('Rok')
# wykres.legend().remove()
# plt.title('Ilość urodzonych dzieci dla każdego roku')
# plt.show()

# Zadanie 2 Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.
# b = df.groupby('Plec').agg({'Liczba': ['sum']})
# wykres = b.plot.bar()
# plt.title('Ilość urodzonych dzieci ze względu na płeć')
# wykres.legend().remove()
# wykres.set_ylabel('Ilość [Mln]')
# plt.show()

# Zadanie 3 Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.

# Zadanie 4 Z repozytorium UCI (http://archive.ics.uci.edu/ml/index.php) pobierz dataset Iris i za pomocą wykresu punktowego (scattered) wyświetl wartość 2 wybranych cech tego datasetu. Dla każdego rodzaju kwiatu użyj innego koloru na wykresie. Przykład można znaleźć w galerii wykresów biblioteki matplotlib - link w materiałach matplotlib.

# Zadanie 5 Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór danych zamówienia.csv).
