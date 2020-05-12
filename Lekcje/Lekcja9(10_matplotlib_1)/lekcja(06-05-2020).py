import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
os.system('cls')
# Zadanie 1
# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20].
# Dodaj etykietę do linii wykresu i wyświetl legendę.
# Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).

# a = []
# for i in range(1, 22):
#     a.append(1/i)
# plt.plot(a)
# plt.xlabel('funkcja 1/x dla x ϵ [1, 20]')
# plt.xticks(np.arange(0, 22, step=1))
# plt.show()

# Zadanie 2
# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.

# a = []
# for i in range(1, 22):
#     a.append(1/i)
# plt.plot(a, 'g:')
# plt.plot(a, 'g>')
# plt.title('Funkcja 1/x dla x ϵ [1, 20]')
# plt.xticks(np.arange(0, 22, step=1))
# plt.show()

# Zadanie 3
# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1. Dodaj etykiety i legendę do wykresu.

# x = np.arange(0, 30, 0.1)
# s = np.sin(x)
# c = np.cos(x)
# plt.plot(x, s, label='sin(x)')
# plt.plot(x, c, label='cos(x)')
# plt.title('Funkcje sin(x) i cos(x)  dla x ϵ [0, 30]')
# plt.legend(loc=4)
# plt.show()

# Zadanie 4
# Dodaj drugi wykres funkcji sinus do zadania 3 i zmodyfikuj parametry funkcji,
# tak aby osiągnąć efekt podobny do tego na poniższym zrzucie ekranu.

# x = np.arange(0, 30, 0.1)
# s = np.sin(x)*-1
# s2 = np.sin(x)+2
# plt.plot(x, s, label='sin(x)')
# plt.plot(x, s2, label='sin(x)')
# plt.title('Wykres sin(x),sin(x)')
# plt.ylabel('sin(x)')
# plt.xlabel('x')
# plt.legend(loc=6)
# plt.show()

# Zadanie 5
# Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris) wygeneruj wykres punktowy,
# gdzie wektor x to wartość ‘sepal length’ a y to ‘sepal width’,
# dodaj paletę kolorów c na przykładzie listingu 6 a parametr s niech będzie wartością absolutną z różnicy wartości poszczególnych elementów wektorów x oraz y.

# df = pd.read_csv("D:\programowanie\wizualizacja danych\Lekcje\Lekcja9(10_matplotlib_1)\iris.data", sep=",", names=[
#                  "sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])
# c = np.random.randint(0, 50, 150)
# x = df['sepal length in cm']
# y = df['sepal width in cm']
# plt.scatter(x, y, c=c)
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()

# Zadanie 6
# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8. Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). Dodaj do wykresów stosowne etykiety. Poustawiaj różne kolory dla wykresów.
# 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie.
# 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla mężczyzn dla każdego roku z osobna. Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.
# 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.


xlsx = pd.ExcelFile(
    'D:\programowanie\wizualizacja danych\Lekcje\Lekcja8(9_pandas_2)\imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')
k=range(2000,2018,1)



a=df.agg({'Liczba': [sum]})  #dzieci ogólnie

b1=df[df['Plec'] == "M"].groupby(['Rok']).agg({'Liczba': [sum]})  #chłopcy na rok
b2=df[df['Plec'] == "K"].groupby(['Rok']).agg({'Liczba': [sum]})  #dziewczynki na rok

c = df.groupby(['Rok']).agg({'Liczba': ['sum']}) #suma urodzinych dzieci na rok

##plt.plot(k, a, label='Ogólnie')

plt.plot(k, b1, label='Chłopcy')
plt.plot(k, b2, label='Dziewczynki')
plt.plot(k, c, label='Ogólnie')


plt.xticks((range(2000,2018,2)))
plt.xlabel('Rok')
plt.ylabel('Ilość')
plt.legend()
plt.show()
# Zadanie 7
# Korzystając z tutoriala pod adresem https://towardsdatascience.com/matplotlib-tutorial-learn-basics-of-pythons-powerful-plotting-library-b5d1b8f67596 lub
# innego zmodyfikuj wykres 2 z zadania 6 tak, aby zamiast wykresu liniowego przedstawiał wykres łupkowy skumulowany
# (czyli jeden słupek dla kobiet i mężczyzn, ale składający się z dwóch „nałożonych” na siebie słupków).


# Zadanie 8
# Napisz funkcję, która losowo rzuca dwiema kostkami k6 n razy. Wynik rzutów zapisywany jest w postaci listy sum oczek z
# tych dwóch kostek. Np. rzucaj(6) generuje 6 rzutów kostkami i zwraca wektor 6 sum oczek każdego rzutu.
# Po zakończeniu funkcji wyświetlaj histogram sumy rzutów. Dodaj stosowne etykiety do wykresu.

# Zadanie 9
# Korzystając z pliku zamówienia.csv (Pandas) policz sumy zamówień dla każdego przedawcy i wyświetl wykres kołowy z
# procentowym udziałem każdego sprzedawcy w ogólnej sumie zamówień. Poszukaj w Internecie jak dodać cień do takiego wykresu i
# jak działa atrybut ‘explode’ tego wykresu. Przetestuj ten atrybut na wykresie.


# Zadanie 10
# Poszukaj w bibliotece wykresów (https://matplotlib.org/gallery/index.html) przykładów z adnotacjami (annotating plots) na
# wykresach i dodaj adnotacje do dwóch wybranych stworzonych wcześniej wykresów.
