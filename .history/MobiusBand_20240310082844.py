import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

# Initialize OpenGL
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
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

    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_cube()
    pygame.display.flip()
    pygame.time.wait(10)
