import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.image import imread

# Load the texture image of the Earth
earth_texture = imread('earth_texture.jpg') / 255.0  # Normalize the color values to be in the range 0-1

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

# Plot the Earth with texture map
ax.plot_surface(x, y, z, facecolors=earth_texture, rstride=4, cstride=4, shade=False)

# Set lighting and shading
ax.set_facecolor('black')
ax.view_init(elev=90, azim=0)

# Hide the axes
ax.axis('off')

# Show the plot
plt.show()
