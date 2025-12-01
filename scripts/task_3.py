from parameters import *


target_x = 30
target_y = 40

def calc_optimal_angle(h, initial_velocity, ay):
    x = target_x
    y = target_y
    v0 = initial_velocity

    discriminant = v0**4 - ay**2 * x**2 + 2 * ay * v0**2 * (y - h)
    if discriminant < 0:
        raise ValueError("The target is unreachable with the given initial velocity and height.")

    T1 = (-v0**2 + np.sqrt(discriminant)) / (ay * x)
    T2 = (-v0**2 - np.sqrt(discriminant)) / (ay * x)

    theta_low = np.arctan(T1)
    theta_high = np.arctan(T2)

    return theta_low, theta_high

def resolve_vectors(initial_velocity, theta_rad):
    vy = initial_velocity * np.sin(theta_rad)
    vx = initial_velocity * np.cos(theta_rad)
    return vy, vx

def calc_flight_time(vy, ay, h,):
    discriminant = (vy)**2 - 2 * ay * h
    if discriminant < 0:
        raise ValueError("The parameters result in complex flight time.")
    
    flight_time = (-vy - np.sqrt(discriminant)) / ay
    return flight_time

def calc_range(vx, flight_time):
    max_range = vx * flight_time
    return max_range

def calc_max_height(vy, ay, h):
    time_to_apogee = (0 - vy) / ay
    max_height = h + vy * time_to_apogee + 0.5 * ay * time_to_apogee**2
    return time_to_apogee, max_height

def y_vals(x, h, theta_rad, vx, ay):
    y = h + np.tan(theta_rad) * x + (ay / (2 * vx**2)) * x**2
    return y

def run_for_thetas(theta_rad):
    vy, vx = resolve_vectors(v0, theta_rad)
    flight_time = calc_flight_time(vy, ay, h)
    max_range = calc_range(vx, flight_time)
    time_to_apogee, max_height = calc_max_height(vy, ay, h)

    pos_x = np.linspace(0, max_range, num=500)
    pos_y = [y_vals(x, h, theta_rad, vx, ay) for x in pos_x]
    return max_height, max_range, flight_time, time_to_apogee, pos_x, pos_y

theta1, theta2 = calc_optimal_angle(h, v0, ay)

output1 = run_for_thetas(theta1)
output2 = run_for_thetas(theta2)

def calc_min_u(ay, target_x, target_y):
    # ay is negative (gravity). use -ay to get a positive value inside the square root
    u_min = np.sqrt(-ay) * np.sqrt(target_y + np.sqrt(target_x**2 + (target_y - h)**2))
    return u_min

def run_for_min_u(u, theta_rad):
    vy, vx = resolve_vectors(u, theta_rad)
    flight_time = calc_flight_time(vy, ay, h)
    max_range = calc_range(vx, flight_time)
    time_to_apogee, max_height = calc_max_height(vy, ay, h)

    pos_x = np.linspace(0, max_range, num=500)
    pos_y = [y_vals(x, h, theta_rad, vx, ay) for x in pos_x]
    return max_height, max_range, flight_time, time_to_apogee, pos_x, pos_y

min_u = calc_min_u(ay, target_x, target_y)
theta_min_low, theta_min_high = calc_optimal_angle(h, min_u, ay)

output_min_low = run_for_min_u(min_u, theta_min_low)
output_min_high = run_for_min_u(min_u, theta_min_high)

print("Low-angle solution:")
print(
    f"Initial height was: {h} m\n"
    f"The max height was: {output1[0]} m\n"
    f"The projectile travelled: {output1[1]} m\n"
    f"The total time of flight was: {output1[2]} s\n"
    f"The time to reach the apogee was: {output1[3]} s\n"
)

print("High-angle solution:")
print(
    f"Initial height was: {h} m\n"
    f"The max height was: {output2[0]} m\n"
    f"The projectile travelled: {output2[1]} m\n"
    f"The total time of flight was: {output2[2]} s\n"
    f"The time to reach the apogee was: {output2[3]} s"
)

print("Minimum initial velocity solution:")
print(
    f"Initial height was: {h} m\n"
    f"Minimum initial velocity was: {min_u} m/s\n"
    f"Low-angle (deg): {np.degrees(theta_min_low)}\n"
    f"  max height: {output_min_low[0]} m\n"
    f"  range: {output_min_low[1]} m\n"
    f"  flight time: {output_min_low[2]} s\n\n"
    f"High-angle (deg): {np.degrees(theta_min_high)}\n"
    f"  max height: {output_min_high[0]} m\n"
    f"  range: {output_min_high[1]} m\n"
    f"  flight time: {output_min_high[2]} s"
)

plt.figure()
plt.plot(output1[4], output1[5], label="Low angle solution")
plt.plot(output2[4], output2[5], label="High angle solution")
plt.plot(output_min_low[4], output_min_low[5], '--', label=f"Min-u low ({np.degrees(theta_min_low)} degrees) u={min_u} m/s")
plt.plot(output_min_high[4], output_min_high[5], '--', label=f"Min-u high ({np.degrees(theta_min_high)} degrees) u={min_u} m/s")
plt.scatter([target_x], [target_y], marker="x", s=80, label=f"Target ({target_x}, {target_y})")
plt.ylabel("Displacement in Y")
plt.title("Drag-free Projectile Motion")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()