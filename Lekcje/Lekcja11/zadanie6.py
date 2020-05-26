from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.gca( projection = '3d' )
            #20 punktów    
x = np.random.sample(20)
y = np.random.sample(20)
# przez użycie zdir='y', wartość y dla tych punktów jest równe zs czyli 0
# punkty (x,y) są nakładane na osiach x i z.
ax.scatter(x, y, zs = 0 , zdir = 'y' ,color="r",  label = 'punkty na (x,z)' )


            #5 punktów      
x = np.random.sample(5)
y = np.random.sample(5)
# przez użycie zdir='y', wartość y dla tych punktów jest równe zs czyli 0
# punkty (x,y) są nakładane na osiach x i z.
ax.plot(x, y, zs = 0 , zdir = 'z' , label = 'linia na (x,y)' )
            
            
# Limity dla legendy
ax.legend()
ax.set_xlim( 0 , 1 )
ax.set_ylim( 0 , 1 )
ax.set_zlim( 0 , 1 )
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )
# Ustawienie kąta nachylenia przy generowaniu wykresu
# oś y=0
ax.view_init( elev = 20. , azim =- 35 )
plt.show()