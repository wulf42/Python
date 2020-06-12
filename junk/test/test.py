import matplotlib.pyplot as plt
import numpy as np

dziedzina = np.arange(0, 12, 0.1)
s = np.sin(dziedzina)
plt.plot(dziedzina, s, label='f(x)= sin(x)')
plt.plot(dziedzina, -s, '--', label='f(x)= -sin(x)')
plt.legend(loc=4)  # loklaizacja legendy
plt.show()
