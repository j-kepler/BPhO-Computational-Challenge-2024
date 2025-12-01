from parameters import *


vy = v0*np.sin(theta_rad)
vx = v0*np.cos(theta_rad)

def calc_flight_time(vy, ay, h,):
    discriminant = vy**2 - 2 * ay * h
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

def resolve_vectors(initial_velocity, theta_rad):
    vy = initial_velocity * np.sin(theta_rad)
    vx = initial_velocity * np.cos(theta_rad)
    return vy, vx

def run_for_thetas(theta_rad):
    vy, vx = resolve_vectors(v0, theta_rad)
    flight_time = calc_flight_time(vy, ay, h)
    max_range = calc_range(vx, flight_time)
    time_to_apogee, max_height = calc_max_height(vy, ay, h)

    pos_x = np.linspace(0, max_range, num=500)
    pos_y = [y_vals(x, h, theta_rad, vx, ay) for x in pos_x]
    return max_height, max_range, flight_time, time_to_apogee, pos_x, pos_y

optimal_theta = np.arcsin((1) / (np.sqrt(2+2 * ay * h / v0**2)))

normal_solution = run_for_thetas(theta_rad)
max_range_solution = run_for_thetas(optimal_theta)

print("Input angle solution:")
print(
    f"For the maximum range solution:\n"
    f"  The optimal angle was: {theta} degrees\n"
    f"  Initial height was: {h} m\n"
    f"  The max height was: {normal_solution[0]} m\n"
    f"  The projectile travelled: {normal_solution[1]} m\n"
    f"  The total time of flight was: {normal_solution[2]} s\n"
    f"  The time to reach the apogee was: {normal_solution[3]} s"
)

print("Maximum range solution:")
print(
    f"The optimal angle was: {np.rad2deg(optimal_theta)} degrees\n"
    f"Initial height was: {h} m\n"
    f"The max height was: {max_range_solution[0]} m\n"
    f"The projectile travelled: {max_range_solution[1]} m\n"
    f"The total time of flight was: {max_range_solution[2]} s\n"
    f"The time to reach the apogee was: {max_range_solution[3]} s"
)

plt.figure()
plt.plot(max_range_solution[4], max_range_solution[5],label=f"Optimal angle ({np.rad2deg(optimal_theta)} degrees) solution")
plt.plot(normal_solution[4], normal_solution[5],label=f"Normal angle ({theta} degrees) solution")
plt.xlabel("Displacement in X")
plt.ylabel("Displacement in Y")
plt.title("Drag-free Projectile Motion")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()