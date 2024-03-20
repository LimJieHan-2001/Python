import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm

def plot_3d_earth():
    # Create a figure and a 3D axis
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Earth parameters
    radius = 6371  # Radius of the Earth in kilometers
    theta = np.linspace(0, 2*np.pi, 100)
    phi = np.linspace(0, np.pi, 100)

    # Convert spherical coordinates to Cartesian coordinates
    x = radius * np.outer(np.cos(theta), np.sin(phi))
    y = radius * np.outer(np.sin(theta), np.sin(phi))
    z = radius * np.outer(np.ones(np.size(theta)), np.cos(phi))

    # Plot the surface of the Earth
    ax.plot_surface(x, y, z, cmap=cm.Blues, linewidth=0, antialiased=False)

    # Set axis limits
    ax.set_xlim([-radius, radius])
    ax.set_ylim([-radius, radius])
    ax.set_zlim([-radius, radius])

    # Hide grid lines
    ax.grid(False)

    # Set aspect ratio to be equal for all axes
    ax.set_box_aspect([1, 1, 1])

    # Set axis labels
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')

    # Set title
    ax.set_title('3D Model of Earth')

    plt.show()

if __name__ == "__main__":
    plot_3d_earth()
