import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

fig, ax = plt.subplots()
im = ax.imshow(u, origin='lower', extent=[0, lx, 0, ly],
               vmin=15, vmax=200, cmap='hot')
plt.colorbar(im)

ax.set_xlabel("x")
ax.set_ylabel("y")
title = ax.set_title("Tid = 0 s")

time = 0
steps_per_frame = 20
def update(frame):
    global u, time

    for _ in range(steps_per_frame):
        u_new = u.copy()

        u_new[1:-1, 1:-1] = u[1:-1, 1:-1] + dt * alpha_field[1:-1, 1:-1] * (
            (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, :-2]) / dx ** 2 +
            (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[:-2, 1:-1]) / dy ** 2
        )
        u = u_new

    im.set_array(u)
    title.set_text(f"Tid = {time:.1f} s")

    return im,

frames = nt // steps_per_frame

ani = FuncAnimation(fig, update, frames=frames, interval=30)

ani.save("solution_extrme_2.gif", writer="pillow", fps=30)
plt.show()
