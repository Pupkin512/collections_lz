import matplotlib.pyplot as plt
import matplotlib as mlt
import numpy as np
def f(x):
    return x**3 + 8*x**2 + x + 6
x = np.arange(1,30,1)
y = f(x)
plt.plot(x,y)
plt.show()
