import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.image import imread

# Load the texture image of the Earth
sphere_texture = imread('sphere_texture.jpg') / 255.0 # Normalize the color values to be in the range 0-1

# Adjust brightness by scaling the color values
brightness_scale = 1.5  # Increase or decrease to adjust brightness
adjusted_sphere_texture = np.clip(sphere_texture * brightness_scale, 0, 1)  # Clip values to be within [0, 1] range

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
ax.plot_surface(x, y, z, facecolors=adjusted_sphere_texture, rstride=4, strive=4, shade=True, alpha=1.0)

# Set lighting
ax.set_facecolor('black')
ax.view_init(elev=25, azim=45)
ax.azim = 150
ax.dist = 8

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Realistic 3D Model of sphere')

# Hide the axes
ax.axis('off')

# Show the plot
plt.show()
