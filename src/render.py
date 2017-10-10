import pygame
from pygame import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import os

import random
import Flock
import Boid
import P3

x = 800
y = 600
z = 1000



bird_vertices = (
            (0, 0, 0),
            (0, 1, .25),
            (-1, 1, 0),
            (0, 1, -.25),
            (1, 1, 0)
            )
ground_vertices = (
    (-100, 100, -.1),
    (100, 100, -.1),
    (-100, -100, -.1),
    (100, -100, -.1)
   )
ground_edges = (
    (0, 1),
    (1, 3),
    (3, 2),
    (2, 0)
)
building_vertices = (
    (0,0,0),#0
    (1,0,0),#1
    (1,0,-1),#2
    (0,0,-1),#3
    (0,1,0),#4
    (1,1,0),#5
    (1,1,-1),#6
    (0,1,-1)#7
    )

#call to create display
def start(x, y, width, hieght, depth):
    os.environ['SDL_VIDEO_WINDOW_POS'] = str(x) + "," + str(y)
    pygame.init()
    display = (width, hieght)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, depth)
    glTranslatef(-10, 30, -250)
    glRotatef(-45, 1, 1, 1)


# draws the ground (render use only)
def ground():
    glBegin(GL_QUADS)
    for edges in ground_edges:
        for vert in edges:
            glColor3fv((0, .5, .5))
            glVertex3fv(ground_vertices[vert])
    glEnd()


#creates vertices for individual birds (render use only)
def make_bird_vertices(bird):
    new_vertices = []

    for vert in bird_vertices:
        new_vert = []

        new_x = vert[0] + bird.position.x
        new_y = vert[1] + bird.position.y
        new_z = vert[2] + bird.position.z

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices



#used to display birds (render use only)
def draw_bird(vertices):
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
            glColor3fv((1,1,1))
            glVertex3fv(vertices[vertex])
    glEnd()



#call to create a new building
class Buildings(object):
    registry = []

    def __init__(self, x, y, width, height, depth, color):
        self.registry.append(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.depth = depth
        self.color = color

    #sets building verts (render use only)
    def set_building(self):
        new_vertices = []
        final_vertices = []
        global building_count

        #scaling
        for nvert in building_vertices:
            fnew_vert = []

            newv_x = nvert[0] * self.width
            newv_y = nvert[1] * self.depth
            newv_z = nvert[2] * self.height

            fnew_vert.append(newv_x)
            fnew_vert.append(newv_y)
            fnew_vert.append(newv_z)

            new_vertices.append(fnew_vert)

        #positoning
        for vert in new_vertices:
            new_vert = []

            new_x = vert[0] + self.x
            new_y = vert[1] + self.y
            new_z = vert[2]

            new_vert.append(new_x)
            new_vert.append(new_y)
            new_vert.append(new_z)

            final_vertices.append(new_vert)

        return final_vertices

    #displays buildings (render use only)
    def draw_building(self):
        edges = (
        (0, 1),
        (0, 4),
        (1, 2),
        (1, 5),
        (2, 3),
        (2, 6),
        (3, 0),
        (3, 7),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4)
        )
        surfaces = (
            (0,1,2,3),
            (2,6,5,1),
            (0,1,4,5),
            (0,3,7,4),
            (3,7,6,2),
            (7,4,5,6)
        )
        vertices = Buildings.set_building(self)
        glBegin(GL_QUADS)
        for surface in surfaces:
            for vertex in surface:
                glColor3fv(self.color)
                glVertex3fv(vertices[vertex])
        glEnd()


        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glColor3fv((1, 1, 1))
                glVertex3fv(vertices[vertex])
        glEnd()

#call to create new flock
class Render:
    def __init__(self, flock):
        self.flock = flock

    #draws objects on screen (call each tick of the clock)
    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        ground()

        for building in Buildings.registry:
            Buildings.draw_building(building)

        for b in self.flock.boids:
            v = make_bird_vertices(b)
            draw_bird(v)



        pygame.display.flip()






if __name__ == "__main__":
    flock = Flock.Flock(100, P3.P3(-75, -75, 0), 10)
    f = Render(flock)

    for num in range(10):
        Buildings(random.randrange(-100, 100), random.randrange(-100, 100), random.randrange(1, 10), random.randrange(1, 10), random.randrange(1, 10), (random.randrange(0,2), random.randrange(0,2), random.randrange(0,2)))

    start(800, 600, 1000)


    while 1:
        f.draw()
        for b in flock.boids:
            b.move_Boid(.1)

