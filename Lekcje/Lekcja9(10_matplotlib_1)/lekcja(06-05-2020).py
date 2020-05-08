import matplotlib.pyplot as plt
import numpy as np
import os

# Zadanie 1
# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20].
# Dodaj etykietę do linii wykresu i wyświetl legendę.
# Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).
# a=[]
# for i in range(1,22):
#     a.append(1/i)
# plt.plot(a)
# plt.xlabel('funkcja 1/x dla x ϵ [1, 20]')
# plt.xticks(np.arange(0, 22, step=1))
# plt.show()
# Zadanie 2
# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.
# a=[]
# for i in range(1,22):
#     a.append(1/i)
# plt.plot(a,'g:')
# plt.plot(a,'g>')
# plt.title('Funkcja 1/x dla x ϵ [1, 20]')
# plt.xticks(np.arange(0, 22, step=1))
# plt.show()