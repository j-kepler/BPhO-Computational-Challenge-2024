from parameters import *


target_x = 30
target_y = 40

def calc_optimal_angle(h, initial_velocity, ay):
    theta_low = np.arctan((-target_x + np.sqrt((-target_x)**2 -4* ay / (2 * initial_velocity ** 2) * target_y - h + (ay * target_x**2) / (2 * initial_velocity ** 2))))
    theta_high = np.arctan((-target_x - np.sqrt((-target_x)**2 -4* ay / (2 * initial_velocity ** 2) * target_y - h + (ay * target_x**2) / (2 * initial_velocity ** 2))))

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

def run_for_thetas (*theta_rad):
    vy, vx = resolve_vectors(Initial_Velocity, theta_rad)
    flight_time = calc_flight_time(vy, ay, h)
    max_range = calc_range(vx, flight_time)
    time_to_apogee, max_height = calc_max_height(vy, ay, h)

    pos_x = np.linspace(0, max_range, num=500)
    pos_y = [y_vals(x, h, theta_rad, vx, ay) for x in pos_x]
    return max_height, max_range, flight_time, time_to_apogee, pos_x, pos_y

theta_low, theta_high = calc_optimal_angle(h, Initial_Velocity, ay)

output_low = run_for_thetas(theta_low)
output_high = run_for_thetas(theta_high)

print("Low-angle solution:")
print(
    f"Initial height was: {h} m\n"
    f"The max height was: {output_low[0]} m\n"
    f"The projectile travelled: {output_low[1]} m\n"
    f"The total time of flight was: {output_low[2]} s\n"
    f"The time to reach the apogee was: {output_low[3]} s\n"
)

print("High-angle solution:")
print(
    f"Initial height was: {h} m\n"
    f"The max height was: {output_high[0]} m\n"
    f"The projectile travelled: {output_high[1]} m\n"
    f"The total time of flight was: {output_high[2]} s\n"
    f"The time to reach the apogee was: {output_high[3]} s"
)

plt.figure()
plt.plot(output_low[4], output_low[5], label="Low angle")
plt.plot(output_high[4], output_high[5], label="High angle")
plt.xlabel("Displacement in X")
plt.ylabel("Displacement in Y")
plt.title("Drag-free Projectile Motion")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()