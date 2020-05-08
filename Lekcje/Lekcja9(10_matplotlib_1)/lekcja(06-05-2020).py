import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
os.system('cls')
# Zadanie 1
# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20].
# Dodaj etykietę do linii wykresu i wyświetl legendę.
# Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).

a = []
for i in range(1, 22):
    a.append(1/i)
plt.plot(a)
plt.xlabel('funkcja 1/x dla x ϵ [1, 20]')
plt.xticks(np.arange(0, 22, step=1))
plt.show()

# Zadanie 2
# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.

a = []
for i in range(1, 22):
    a.append(1/i)
plt.plot(a, 'g:')
plt.plot(a, 'g>')
plt.title('Funkcja 1/x dla x ϵ [1, 20]')
plt.xticks(np.arange(0, 22, step=1))
plt.show()

# Zadanie 3
# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1. Dodaj etykiety i legendę do wykresu.

x = np.arange(0, 30, 0.1)
s = np.sin(x)
c = np.cos(x)
plt.plot(x, s, label='sin(x)')
plt.plot(x, c, label='cos(x)')
plt.title('Funkcje sin(x) i cos(x)  dla x ϵ [0, 30]')
plt.legend(loc=4)
plt.show()

# Zadanie 4
# Dodaj drugi wykres funkcji sinus do zadania 3 i zmodyfikuj parametry funkcji,
# tak aby osiągnąć efekt podobny do tego na poniższym zrzucie ekranu.

x = np.arange(0, 30, 0.1)
s = np.sin(x)*-1
s2 = np.sin(x)+2
plt.plot(x, s, label='sin(x)')
plt.plot(x, s2, label='sin(x)')
plt.title('Wykres sin(x),sin(x)')
plt.ylabel('sin(x)')
plt.xlabel('x')
plt.legend(loc=6)
plt.show()

# Zadanie 5
# Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris) wygeneruj wykres punktowy,
# gdzie wektor x to wartość ‘sepal length’ a y to ‘sepal width’,
# dodaj paletę kolorów c na przykładzie listingu 6 a parametr s niech będzie wartością absolutną z różnicy wartości poszczególnych elementów wektorów x oraz y.

df = pd.read_csv("D:\programowanie\wizualizacja danych\Lekcje\Lekcja9(10_matplotlib_1)\iris.data", sep=",", names=[
                 "sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])
c = np.random.randint(0, 50, 150)
x = df['sepal length in cm']
y = df['sepal width in cm']
plt.scatter(x, y, c=c)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()
