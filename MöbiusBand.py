import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Initialize OpenGL
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Define cube vertices, edges, and faces
vertices = [
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, -1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),
    (1, 5),
    (2, 7),
    (3, 6),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4)
]

# Define initial rotation angles
angle_x = 0
angle_y = 0
angle_z = 0

# Function to draw the cube
def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Keyboard controls
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle_y += 1
            elif event.key == pygame.K_RIGHT:
                angle_y -= 1
            elif event.key == pygame.K_UP:
                angle_x += 1
            elif event.key == pygame.K_DOWN:
                angle_x -= 1

        # Mouse controls
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                glTranslatef(0, 0, 1.0)
            elif event.button == 5:
                glTranslatef(0, 0, -1.0)

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Apply rotation transformations
    glRotatef(angle_x, 1, 0, 0)
    glRotatef(angle_y, 0, 1, 0)
    glRotatef(angle_z, 0, 0, 1)

    # Draw the cube
    draw_cube()

    # Update display
    pygame.display.flip()
    pygame.time.wait(10)
