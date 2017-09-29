# Boid Project
# OpenGL Rendering


import pygame
from pygame import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

x = 800
y = 600
z = 1000

bird_count = 0
bird_dict = {}

bird_vertices = (
    (0, 0, 0),
    (0, .25, 1),
    (-1, 0, 1),
    (0, -.25, 1),
    (1, 0, 1)
)
ground_vertices = (
    (-100, -.1, 250),
    (100, -.1, 250),
    (-100, -.10, -10),
    (100, -.10, -10)
)


def ground():
    glBegin(GL_QUADS)
    for verts in ground_vertices:
        glColor3fv((0, .5, .5))
        glVertex3fv(verts)
    glEnd()


def set_bird_vertices(x, y, z, birdNum=None):
    new_vertices = []
    global bird_count

    for vert in bird_vertices:
        new_vert = []

        new_x = vert[0] + x
        new_y = vert[1] + y
        new_z = vert[2] + z

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)


    if not birdNum:
        bird_dict[bird_count] = new_vertices
        bird_count += 1
    else:
        bird_dict[birdNum] = new_vertices

    return


class bird():
    def __init__(self, vertices):
        edges = (
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (1, 2),
            (1, 4),
            (3, 2),
            (3, 4)
        )
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glColor3fv((1, 1, 1))
                glVertex3fv(vertices[vertex])
        glEnd()


class Matrix():
    # matrix = [4][4]
    def __init__(self):
        self.matrix = [4][4]
        self.matrix[0][0] = 1
        self.matrix[1][1] = 1
        self.matrix[2][2] = 1
        self.matrix[3][3] = 1

    def multiply(self, m):
        result = Matrix()
        a = [4][4]
        b = [4][4]
        c = result.matrix
        for i in range(4):
            for j in range(4):
                c[i][j] = 0
                for k in range(4):
                    c[i][j] += a[i][k] * b[k][j]

        return result


def display():
    pygame.init()
    display = (x, y)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 150)

    glTranslatef(0, -10, -20)

    glRotatef(0, 0, 0, 0)
    vet_1 = [-20, -20, -30]
    set_bird_vertices(*vet_1, 100)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glTranslatef(0.0, 0.0, -1)
        vet_1 = [vet_1[0] + 1, vet_1[0] + 1, -30]
        set_bird_vertices(*vet_1, 1)
        ground()
        for each_bird in bird_dict:
            bird(bird_dict[each_bird])

        # glTranslatef(0, 0, -2)
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    for num in range(100):
        set_bird_vertices(random.randrange(-20, 20), random.randrange(-20, 20), random.randrange(-100, 0))
    display()


