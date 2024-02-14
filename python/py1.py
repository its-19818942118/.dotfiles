import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create an array of theta values in degrees (e.g., from 0 to 113*360 degrees)
theta_degrees = np.linspace(0, 113 * 360, 10000)

# Convert degrees to radians
theta_radians = np.deg2rad(theta_degrees)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
plt.gca().set_facecolor('black')
ax.set_aspect('equal')
plt.grid(False)
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)

# Initialize an empty line for the plot
line, = ax.plot([], [], color='white', linewidth=0.5)

# Function to update the plot with a new frame
def update(frame):
    # Calculate z(theta) using the formula
    z = np.exp(frame * theta_radians * 1j) + np.exp(np.pi * frame * theta_radians * 1j)

    # Separate the real and imaginary parts of z
    x = np.real(z)
    y = np.imag(z)

    # Update the line data
    line.set_data(x, y)

# Create an animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 113, 226), repeat=True, interval=50)

plt.show()

