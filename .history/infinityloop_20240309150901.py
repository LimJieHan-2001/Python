import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Initialize Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Initialize OpenGL
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

def infinity_loop(radius, num_segments, num_twists):
    vertices = []
    for i in range(num_segments):
        theta = i * 2 * np.pi / num_segments
        phi = num_twists * theta
        x = radius * np.sin(theta)
        y = radius * np.cos(theta)
        z = radius * np.sin(phi)
        vertices.append([x, y, z])
    return vertices

def draw_infinity_loop(vertices):
    glBegin(GL_LINE_STRIP)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    infinity_vertices = infinity_loop(radius=1, num_segments=100, num_twists=2)
    draw_infinity_loop(infinity_vertices)

    pygame.display.flip()
    pygame.time.wait(10)
