import numpy as np
import matplotlib.pyplot as plt

# FYSISKE PARAMETERE
alpha = 9.3e-6   # termisk diffusivitet

# GEOMETRI
Lx = 0.25   # bredde i meter
Ly = 0.25   # høyde i meter

# DISKRETISERING
Nx = 60
Ny = 60

dx = Lx / Nx
dy = Ly / Ny

# Stabilitet
dt = 0.25 * min(dx, dy)**2 / alpha

# Antall tidsskritt
Nt = 2000

# INITIALBETINGELSE
u = np.ones((Nx+1, Ny+1)) * 15.0   # 15 grader i hele legemet

# RANDBETINGELSER
def apply_boundary(u):
    u[0, :] = 200
    u[-1, :] = 200
    u[:, 0] = 200
    u[:, -1] = 200
    return u

u = apply_boundary(u)

# LAGRING AV RESULTATER FOR PLOTTING
times_to_plot = [0, 200, 800, 2000]
solutions = {}

# TIDSLØKKE
for n in range(Nt+1):
    u_new = u.copy()

    # Indre punkter
    for i in range(1, Nx):
        for j in range(1, Ny):
            u_new[i, j] = (
                u[i, j]
                + alpha * dt * (
                    (u[i+1, j] - 2*u[i, j] + u[i-1, j]) / dx**2 +
                    (u[i, j+1] - 2*u[i, j] + u[i, j-1]) / dy**2
                )
            )

    u = apply_boundary(u_new)

    if n in times_to_plot:
        solutions[n] = u.copy()
# PLOTTING
fig, axes = plt.subplots(1, len(times_to_plot), figsize=(15, 4))

for ax, t in zip(axes, times_to_plot):
    im = ax.imshow(solutions[t].T, origin='lower', cmap='jet',
                   extent=[0, Lx, 0, Ly])
    ax.set_title(f"t = {t*dt:.2f} s")
    plt.colorbar(im, ax=ax)
plt.tight_layout()
plt.show()