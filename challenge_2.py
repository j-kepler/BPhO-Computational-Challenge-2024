import matplotlib.pyplot as plt
import numpy as np

g = -9.81

Initial_Height = 0
theta = 45
Initial_Velocity = 30
ax = 0
ay = g

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

def calc_flight_time(vy, ay,):
    flight_time = (2 * (0 - vy)) / ay
    return flight_time

def calc_max_range(vx, flight_time):
    max_range = vx * flight_time
    return max_range

def calc_max_height(vy, ay,):
    time_to_apogee = (0 - vy) / ay
    max_height = vy * time_to_apogee + 0.5 * ay * time_to_apogee**2
    return max_height

flight_time = calc_flight_time(vy, ay)
max_range = calc_max_range(vx, flight_time)
max_height = calc_max_height(vy, ay)

pos_x = np.linspace(0, max_range, num=500)

def y_vals(x, theta_rad, vx, ay):
    y = np.tan(theta_rad) * x + (ay / (2 * vx**2)) * x**2
    return y

pos_y = [y_vals(x, theta_rad, vx, ay) for x in pos_x]

print (f"The max height was: {max_height}m \nThe projectile travelled: {max_range}m \nThe total time of flight was: {flight_time}s")

plt.figure()
plt.plot(pos_x, pos_y)
plt.xlabel("Displacement in X")
plt.ylabel("Displacement in Y")
plt.title("Drag-free Projectile Motion")
plt.grid(True)
plt.tight_layout()
plt.show()