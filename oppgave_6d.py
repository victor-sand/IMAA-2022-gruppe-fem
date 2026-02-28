import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

nodes = 100
lx = 0.25
ly = 0.25
alpha = 9.3e-6

dx = lx / nodes
dy = ly / nodes

dt = 0.9 / (2 * alpha * (1 / dx ** 2 + 1 / dy ** 2))
T = 10 * 60
nt = int(T / dt)

x = np.linspace(0, lx, nodes)
y = np.linspace(0, ly, nodes)

u = np.ones((nodes, nodes)) * 15

# Randbetingelser
u[0, :] = 200
u[-1, :] = 200
u[:, 0] = 200
u[:, -1] = 200

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

        u_new[1:-1, 1:-1] = u[1:-1, 1:-1] + dt * alpha * (
            (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, :-2]) / dx ** 2 +
            (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[:-2, 1:-1]) / dy ** 2
        )

        u = u_new
        time += dt

    im.set_array(u)
    title.set_text(f"Tid = {time:.1f} s")

    return im,

frames = nt // steps_per_frame

ani = FuncAnimation(fig, update, frames=frames, interval=30)

ani.save("solution_extrme_2.gif", writer="pillow", fps=30)
plt.show()
