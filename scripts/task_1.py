from parameters import *


vy = v0*np.sin(theta_rad)
vx = v0*np.cos(theta_rad)

time = [0, ]
pos_y = [h, ]
pos_x = [0, ]

while disp_y >= 0:
    vy += dt * ay

    vx += dt * ax

    disp_y += vy * dt
    pos_y.append (disp_y)

    disp_x += vx *dt
    pos_x.append (disp_x)

    t += dt
    time.append (t)


print (
    f"The max height was: {max(pos_y)}m \n"
    f"The projectile travelled: {max(pos_x)}m \n"
    f"The total time of flight was: {len(time)*dt}s"
)

plt.figure()
plt.plot(pos_x, pos_y)
plt.xlabel("Displacement in X")
plt.ylabel("Displacement in Y")
plt.title("Drag-free Projectile Motion")
plt.grid(True)
plt.tight_layout()
plt.show()