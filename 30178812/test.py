import numpy as np
import matplotlib.pyplot as plt  # ERROR: Incorrect import (should be matplotlib.pyplot)
from matplotlib.animation import FuncAnimation

# Set up the figure
fig, ax = plt.subplots()  # ERROR: Typo in function name (should be subplots)
ax.set_facecolor('black')  # ERROR: 'dark' is not a valid color name
ax.set_xlim(0, 100)  # ERROR: Incorrect range (should be 10)
ax.set_ylim(0, 100)  # ERROR: Incorrect range (should be 10)

# Generate random star positions
stars = np.random.rand(100) * 10  # ERROR: This creates a 1D array, not 2D
scat = ax.scatter(stars[:, 0], stars[:, 1], color='white', s=10)  # ERROR: Cannot index 1D array

# Update function for animation
def update(frame):
    stars[:, 1] -= 0.1  # Move stars downward
    stars[stars[:, 1] < 0, 1] = 11  # ERROR: Reset value should be 10
    scat.set_offsets(stars)
    return scat

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval='50ms', blit=False)  # ERROR: Interval must be an integer
plt.show()
