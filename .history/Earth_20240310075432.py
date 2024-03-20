import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.image import imread

# Load the texture image of the Earth
earth_texture = imread('earth.png') / 255.0  # Normalize the color values to be in the range 0-1

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
ax.plot_surface(x, y, z, facecolors=earth_texture, rstride=4, cstride=4, alpha=1.0, linewidth=0, cmap='gray')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Realistic 3D Model of Earth')

# Hide the axes
ax.axis('off')

# Add lighting
ax.light_sources = [(0, 0, 1)]

# Show the plot
plt.show()

