import matplotlib.pyplot as plt
import numpy as np

g = -9.81

Initial_Height = 0
theta = 45
Initial_Velocity = 30
ax = 0
ay = g
dt = 0.0001

theta_rad = np.deg2rad(theta)

vy = Initial_Velocity*np.sin(theta_rad)
vx = Initial_Velocity*np.cos(theta_rad)
disp_y = Initial_Height
disp_x = 0

t = 0

time = [0, ]
velocity_y = [vy, ]
velocity_x = [vx, ]
pos_y = [Initial_Height, ]
pos_x = [0, ]


while disp_y >= 0:
    vy += dt * ay
    velocity_y.append (vy)

    vx += dt * ax
    velocity_x.append (vx)

    disp_y += vy * dt
    pos_y.append (disp_y)

    disp_x += vx *dt
    pos_x.append (disp_x)

    t += dt
    time.append (t)


print (f"The max height was: {max(pos_y)}m \nThe projectile travelled: {max(pos_x)}m \nThe total time of flight was: {len(time)*dt}s")

plt.figure()
plt.plot(pos_x, pos_y)
plt.xlabel("Displacement in X")
plt.ylabel("Displacement in Y")
plt.title("Drag-free Projectile Motion")
plt.grid(True)
plt.tight_layout()
plt.show()