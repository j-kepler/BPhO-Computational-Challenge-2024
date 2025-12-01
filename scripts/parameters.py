import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


h = 20
theta = 45
v0 = 30
ax = 0
ay = -9.81
t = 0
dt = 0.0001

theta_rad = np.deg2rad(theta)

disp_y = h
disp_x = 0