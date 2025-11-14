from parameters import *


def calc_flight_time(vy, ay, h,):
    discriminant = vy**2 - 2 * ay * h
    if discriminant < 0:
        raise ValueError("The parameters result in complex flight time.")
    
    flight_time = (-vy - np.sqrt(discriminant)) / ay
    return flight_time

def calc_max_range(vx, flight_time):
    max_range = vx * flight_time
    return max_range

def calc_max_height(vy, ay, h):
    time_to_apogee = (0 - vy) / ay
    max_height = h + vy * time_to_apogee + 0.5 * ay * time_to_apogee**2
    return time_to_apogee, max_height

def y_vals(x, h, theta_rad, vx, ay):
    y = h + np.tan(theta_rad) * x + (ay / (2 * vx**2)) * x**2
    return y

flight_time = calc_flight_time(vy, ay, Initial_Height)
max_range = calc_max_range(vx, flight_time)
time_to_apogee, max_height = calc_max_height(vy, ay, Initial_Height)

pos_x = np.linspace(0, max_range, num=500)
pos_y = [y_vals(x, Initial_Height, theta_rad, vx, ay) for x in pos_x]

print(
    f"Initial height was: {Initial_Height} m\n"
    f"The max height was: {max_height} m\n"
    f"The projectile travelled: {max_range} m\n"
    f"The total time of flight was: {flight_time} s\n"
    f"The time to reach the apogee was: {time_to_apogee} s"
)

plt.figure()
plt.plot(pos_x, pos_y)
plt.xlabel("Displacement in X")
plt.ylabel("Displacement in Y")
plt.title("Drag-free Projectile Motion")
plt.grid(True)
plt.tight_layout()
plt.show()