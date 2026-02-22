import numpy as np
import matplotlib.pyplot as plt

a, b = -1, 1

def f(x):
    return -(1/np.pi)*np.cos(np.pi*x) + ((1/np.pi**2) + 1)*x + 1

x_vals = np.linspace(a, b, 1000)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
