import numpy as np
import matplotlib.pyplot as plt

# Constants
TIME_STEPS = 10
DELTA_T = 1 # Time step in hours
SLOPE = -0.12  # Slope for temperature decay
INITIAL_TEMPERATURE = 1.0  # Initial temperature

# Function to update temperature using a linear equation
def update_temperature(temperature, slope, delta_t):
    return temperature + slope * delta_t

# Main simulation loop
temperatures = []
current_temperature = INITIAL_TEMPERATURE

for step in range(TIME_STEPS):
    temperatures.append(current_temperature)
    current_temperature = update_temperature(current_temperature, SLOPE, DELTA_T)

# Plotting the temperature evolution
time_points = np.arange(0, TIME_STEPS * DELTA_T, DELTA_T)
plt.plot(time_points, temperatures, label='Temperature')
plt.title('Temperature Evolution Over Time (Linear Decay)')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature')
plt.legend()
plt.show()
