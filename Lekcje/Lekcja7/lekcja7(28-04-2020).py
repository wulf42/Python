import pandas as pd
import numpy as np

# Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
print(s)

# DataFrame
# tworzenie dataframe na podstawie słownika
data = {'Kraj': ['Belgia',  'Indie',  'Brazylia'],
'Stolica': ['Bruksela',  'New Delhi',  'Brasilia'],
'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data,columns=['Kraj',  'Stolica',  'Populacja'])
print(df)
# DataFrame przechowuje typ dla każdej kolumny co możemy sprawdzić wypisując
print(df.dtypes)
# możemy również w prosty sposób stworzyć serię danych - czyli próbki dla kolejnych
# dat, pomiarów czasu
daty = pd.date_range('20180401', periods=5)
print(daty)
df = pd.DataFrame(np.random.randn(5,4), index=daty, columns=list('ABCD'))
print(df)

# biblioteka Pandas umożliwia również tworzenie DataFrame'ów z zewnętrznych źródeł danych
# CSV, odczyt i zapis
df = pd.read_csv('dane.csv', header=None, nrows=2)
print(df)
df.to_csv('plik.csv', header=None, index=False)

# Excel - wymagana bibioteka xlrd oraz openpyxl
import xlrd
import openpyxl

xlsx = pd.ExcelFile('dane.xlsx')
df = pd.read_excel(xlsx,'Punktacja')
print(df)
df.to_excel('z_indeksami.xlsx',  sheet_name='Wydatki z indeksami')

# biblioteka Pandas może również dzięki bibliotece sqlalchemy odczytywać
# dane bezpośrednio z baz danych, lub zapisywać je do SQL-a
# ten temat wykracza jednak poza zakres aktualnej lekcji i może
# zostanie zaprezentowany w lekcji polegającej na wyświetlaniu wykresów na postawie
# danych pochodzących z plików i zewnętrznych źródeł