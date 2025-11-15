import numpy as np
import matplotlib.pyplot as plt


h = 20
theta = 45
Initial_Velocity = 30
ax = 0
ay = -9.81
t = 0
dt = 0.0001

theta_rad = np.deg2rad(theta)

vy = Initial_Velocity*np.sin(theta_rad)
vx = Initial_Velocity*np.cos(theta_rad)
disp_y = h
disp_x = 0

time = [0, ]
pos_y = [h, ]
pos_x = [0, ]