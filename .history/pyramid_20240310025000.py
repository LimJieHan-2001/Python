import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vertices of the pyramid
vertices = np.array([
    [0, 0, 0],   # Apex
    [1, 0, 1],   # Base vertex 1
    [1, 0, -1],  # Base vertex 2
    [-1, 0, -1], # Base vertex 3
    [-1, 0, 1]   # Base vertex 4
])

# Define the triangular faces of the pyramid
faces = np.array([
    [0, 1, 2],
    [0, 2, 3],
    [0, 3, 4],
    [0, 4, 1],
    [1, 2, 3],
    [1, 3, 4]    # Base face
])

# Create a new figure
fig = plt.figure()

# Add a 3D subplot
ax = fig.add_subplot(111, projection='3d')

# Plot the faces as solid surfaces
for face in faces:
    ax.add_collection3d(plt.Poly3DCollection([vertices[face]], color='blue', alpha=0.5))

# Plot the vertices
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='red')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Model of Pyramid')

# Set the viewing angle
ax.view_init(elev=30, azim=45)

# Show the plot
plt.show()
