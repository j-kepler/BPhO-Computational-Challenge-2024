from parameters import *


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