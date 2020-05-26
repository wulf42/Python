from random import choice
import os
os.system('cls')

# 1 Pakoca Wojciech zestaw_20200513_ISI2_1


def zadanie7():
    kolor = ['pik', 'kier', 'trefl', 'karo']
    figura = ['2', '3', '4', '5', '6', '7', '8',
              '9', '10', 'Walet', 'Dama', 'Król', 'As']
    x = []

    for n in range(52):
        x.append(choice(figura) + '  ' + choice(kolor))
    gracze=[x[0:5],x[5:10],x[10:15],x[15:20]]
    for gracz in gracze: print(gracz)

zadanie7()
