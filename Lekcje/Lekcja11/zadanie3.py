import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure(figsize=(8, 8))
ax1 = fig.add_subplot(321, projection='3d')
ax2 = fig.add_subplot(323, projection='3d')
ax3 = fig.add_subplot(325, projection='3d')
ax4 = fig.add_subplot(222, projection='3d')
ax5 = fig.add_subplot(224, projection='3d')
# generuj dane.
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
# rysuj powierzchnię.
surf1 = ax1.plot_surface(X, Y, Z, cmap =cm.Dark2, linewidth = 0 , antialiased = False )
ax1.set_zlim(- 1.01 , 1.01 )
ax1.zaxis.set_major_locator(LinearLocator( 10 ))
ax1.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))

surf2 = ax2.plot_surface(X, Y, Z, cmap =cm.Pastel1, linewidth = 0 , antialiased = False )
ax2.set_zlim(- 1.01 , 1.01 )
ax2.zaxis.set_major_locator(LinearLocator( 10 ))
ax2.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))

surf3 = ax3.plot_surface(X, Y, Z, cmap =cm.Spectral, linewidth = 0 , antialiased = False )
ax3.set_zlim(- 1.01 , 1.01 )
ax3.zaxis.set_major_locator(LinearLocator( 10 ))
ax3.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))


surf4 = ax4.plot_surface(X, Y, Z, cmap =cm.tab10, linewidth = 0 , antialiased = False )
ax4.set_zlim(- 1.01 , 1.01 )
ax4.zaxis.set_major_locator(LinearLocator( 10 ))
ax4.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))


surf5 = ax5.plot_surface(X, Y, Z, cmap =cm.hsv, linewidth = 0 , antialiased = False )
ax5.set_zlim(- 1.01 , 1.01 )
ax5.zaxis.set_major_locator(LinearLocator( 10 ))
ax5.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
plt.show()
