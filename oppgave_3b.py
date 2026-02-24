import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,100)
dx = x[1]-x[0]
f = np.cos(np.pi*x)
u = np.zeros(len(x))
u[0] = 0
u[-1] = 2

for it in range(5000):
    for i in range(1,len(x)-1):
        u[i] = 0.5*(u[i+1]+u[i-1]-dx**2*f[i])

a = x - np.cos(np.pi*x)/np.pi**2 + 1-1/np.pi**2
plt.plot(x,u)
plt.plot(x,a)
plt.show()
