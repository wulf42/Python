import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
os.system('cls')

# korzystając z funkcji random oraz date_range możemy wygenerować szereg czasowy danych
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
# funkcja biblioteki Pandas generująca skumulowana sumę kolejnych elementów
ts = ts.cumsum()
print(ts)
ts.plot()
plt.show()