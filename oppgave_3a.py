import numpy as np
import matplotlib.pyplot as plt

a, b = -1, 1
n = 100

def u(x):
    return -(1/np.pi)*np.cos(np.pi*x) + ((1/np.pi**2) + 1)*x + 1



x_vals = np.linspace(a, b, n)
if __name__ == '__main__':
    print(u(a))
    print(u(b))

    y_vals = u(x_vals)

    plt.plot(x_vals, y_vals)
    plt.xlabel("x")
    plt.ylabel("u(x)")
    plt.grid(True)
    plt.show()
