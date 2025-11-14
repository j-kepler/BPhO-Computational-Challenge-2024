import numpy as np
import matplotlib.pyplot as plt


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