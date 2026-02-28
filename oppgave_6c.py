import numpy as np
import matplotlib.pyplot as plt

nodes = 100
lx = 0.25
ly = 0.25
alpha = 9.3e-6

dx = lx/nodes
dy = ly/nodes

dt = 0.9 / (2*alpha*(1/dx**2 + 1/dy**2))

x = np.linspace(0, lx, nodes)
y = np.linspace(0, ly, nodes)

u = np.ones((nodes, nodes)) * 15

# Randbetingelser
u[0, :] = 200
u[-1, :] = 200
u[:, 0] = 200
u[:, -1] = 200

# kjernen
center_i = nodes // 2
center_j = nodes // 2

target_temp = 60
time = 0
max_time = 20 * 60

while u[center_i, center_j] < target_temp and time < max_time:
    u_new = u.copy()

    u_new[1:-1, 1:-1] = u[1:-1, 1:-1] + dt*alpha*(
        (u[1:-1, 2:] - 2*u[1:-1, 1:-1] + u[1:-1, :-2]) / dx**2 +
        (u[2:, 1:-1] - 2*u[1:-1, 1:-1] + u[:-2, 1:-1]) / dy**2
    )

    u = u_new
    time += dt

print(f"Tiden det tar før kjernen når 60°C er ca: {time:.2f} sekunder")
print(f"Det tilsvarer ca: {time/60:.2f} minutter")

# 3D plot
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, u, cmap='viridis')
fig.colorbar(surf)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Temperatur')
ax.set_title(f"Når kjernen er 60°C\nTid = {time/60:.2f} min")

plt.show()