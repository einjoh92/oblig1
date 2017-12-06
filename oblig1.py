import numpy as np

def piecewise(x):
    if x < -5:
        return -1
    elif x > 5:
        return 1
    else:
        return 0

x = np.linspace(-10,10,100)
f = np.vectorize(piecewise)
y = f(x)


import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()
