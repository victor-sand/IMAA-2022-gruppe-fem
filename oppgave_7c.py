import numpy as np
import matplotlib.pyplot as plt

nodes = 100
air = 0.125   # luft på hver side
lx = 0.25 + 2*air
ly = 0.25 + 2*air
alpha_titan = 9.3e-6
alpha_air = 4.8e-5
start_temp = 15
oven_temp = 200
minutes = 1

dx = lx / nodes
dy = ly / nodes

plate_start = nodes // 4
plate_end = 3 * nodes // 4

alpha_field = np.ones((nodes, nodes)) * alpha_air
alpha_field[
    plate_start:plate_end,
    plate_start:plate_end
] = alpha_titan

alpha_max = max(alpha_titan, alpha_air)

dt = 0.9 / (2 * alpha_max * (1/dx**2 + 1/dy**2))
T = minutes * 60
nt = int(T / dt)

x = np.linspace(0, lx, nodes)
y = np.linspace(0, ly, nodes)

u = np.ones((nodes, nodes)) * oven_temp
u[
    plate_start:plate_end,
    plate_start:plate_end
] = start_temp

# Randbetingelser
u[0, :] = oven_temp
u[-1, :] = oven_temp
u[:, 0] = oven_temp
u[:, -1] = oven_temp

# Kjernen
center_i = nodes // 2
center_j = nodes // 2

target_temp = 60
time = 0
max_time = 20 * 60

while u[center_i, center_j] < target_temp and time < max_time:
    u_new = u.copy()

    u_new[1:-1, 1:-1] = u[1:-1, 1:-1] + dt * alpha_field[1:-1, 1:-1] * (
        (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, :-2]) / dx ** 2 +
        (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[:-2, 1:-1]) / dy ** 2
    )
    u = u_new
    time += dt

print(f"Tiden det tar før kjernen når 60°C er ca: {time:.2f} sekunder")
print(f"Det tilsvarer ca: {time/60:.2f} minutter")

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
