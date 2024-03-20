import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create vertices of the pyramid
vertices = np.array([
    [0, 0, 0],  # Apex
    [1, 0, 1],  # Base vertex 1
    [1, 0, -1], # Base vertex 2
    [-1, 0, -1],# Base vertex 3
    [-1, 0, 1]  # Base vertex 4
])

# Create faces of the pyramid
faces = np.array([
    [0, 1, 2],
    [0, 2, 3],
    [0, 3, 4],
    [0, 4, 1],
    [1, 2, 3, 4]
])

# Plot the pyramid
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for face in faces:
    ax.add_collection3d(plt.Poly3DCollection([vertices[face]]))

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Model of Pyramid')

# Set the aspect ratio of the plot to be equal
ax.set_box_aspect([1,1,1])

# Show the plot
plt.show()
