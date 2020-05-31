import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
# generuj dane.
X = np.arange(- 5, 5, 0.25)
Y = np.arange(- 5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)
# rysuj powierzchnię.


surf = ax1.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)
ax1.set_zlim(- 1.01, 1.01)
ax1.zaxis.set_major_locator(LinearLocator(10))
ax1.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax1.set_title('Wykres pierwotny')
# generuj dane. 2
X = np.arange(- 5, 5, 0.1)
Y = np.arange(- 5, 5, 0.1)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)
surf = ax2.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=True,   )
ax2.set_zlim(- 1.01, 1.01)
ax2.zaxis.set_major_locator(LinearLocator(10))
ax2.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax2.set_title('Wykres zmieniony')


plt.show()
