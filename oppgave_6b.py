import numpy as np
import matplotlib.pyplot as plt

nodes = 100
lx = 0.25
ly = 0.25
alpha = 9.3e-6
start_temp = 15
oven_temp = 200
minutes = 20

dx = lx / nodes
dy = ly / nodes

dt = 0.9 / (2 * alpha * (1 / dx ** 2 + 1 / dy ** 2))
T = minutes * 60
nt = int(T / dt)

x = np.linspace(0, lx, nodes)
y = np.linspace(0, ly, nodes)

u = np.ones((nodes, nodes)) * start_temp

u[0, :] = oven_temp
u[-1, :] = oven_temp
u[:, 0] = oven_temp
u[:, -1] = oven_temp

for _ in range(nt):
    u_new = u.copy()

    u_new[1:-1, 1:-1] = u[1:-1, 1:-1] + dt * alpha * (
        (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, :-2]) / dx ** 2 +
        (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[:-2, 1:-1]) / dy ** 2
    )

    u = u_new

# 3D plot
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, u, cmap='viridis', vmin=start_temp, vmax=oven_temp)
fig.colorbar(surf)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlim(start_temp, oven_temp)
ax.set_zlabel('Temperatur')

plt.show()
