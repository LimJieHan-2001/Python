import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.image import imread

# Load the texture image of the Earth
earth_texture = imread('earth_texture.jpg') / 255.0

# Adjust brightness by scaling the color values
brightness_scale = 1.5  # Increase or decrease to adjust brightness
adjusted_earth_texture = np.clip(earth_texture * brightness_scale, 0, 1)  # Clip values to be within [0, 1] range

# Create a sphere representing the Earth
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 50)
u, v = np.meshgrid(u, v)
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)

# Create a new figure
fig = plt.figure()

# Add a 3D subplot
ax = fig.add_subplot(111, projection='3d')

# Plot the Earth with adjusted brightness texture map
ax.plot_surface(x, y, z, facecolors=adjusted_earth_texture, rstride=4, cstride=4, shade=True, alpha=1.0)

# Set lighting
ax.set_facecolor('black')
ax.view_init(elev=25, azim=45)
ax.azim = 150
ax.dist = 8

# Hide the axes
ax.axis('off')

# Show the plot
plt.show()
