import pygame
from pygame import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import os

import Buildings
import random
import Flock
import Boid
import P3

x_move = 0
y_move = 0
z_move = 0
rotate_x = 0
rotate_y = 0
rotate_z = 0

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



#call to create new flock
class Render:

    def __init__(self, flock):
        self.flock = flock

    @staticmethod
    def move_camera(event):
        global x_move
        global y_move
        global z_move
        global rotate_x
        global rotate_y
        global rotate_z
        if event.key == K_LEFT:
            x_move = 10
        if event.key == K_RIGHT:
            x_move = -10
        if event.key == K_UP:
            y_move = -10
        if event.key == K_DOWN:
            y_move = 10
        if event.key == K_z:
            z_move = 10
        if event.key == K_x:
            z_move = -10
        if event.key == K_a:
            rotate_x = 10
        if event.key == K_d:
            rotate_x = -10
        if event.key == K_w:
            rotate_y = 10
        if event.key == K_s:
            rotate_y = -10
        if event.key == K_q:
            rotate_z = 10
        if event.key == K_e:
            rotate_z = -10
    #draws objects on screen (call each tick of the clock)
    def draw(self):
        global x_move
        global y_move
        global z_move
        global rotate_x
        global rotate_y
        global rotate_z
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                Render.move_camera(event)
            if event.type == pygame.KEYUP:
                x_move = 0
                y_move = 0
                z_move = 0
                rotate_x = 0
                rotate_y = 0
                rotate_z = 0
                if event.type == K_UP or event.type == K_DOWN:
                    Render.move_camera(event)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glTranslate(x_move, y_move, z_move)
        glRotatef(rotate_x, 1.0, 0.0, 0.0)
        glRotatef(rotate_y, 0.0, 1.0, 0.0)
        glRotatef(rotate_z, 0.0, 0.0, 1.0)
        #glRotatef(rotate, 0.0)
        ground()

        for building in Buildings.Buildings.registry:
            Buildings.Buildings.draw_building(building)

        for b in self.flock.boids:
            v = make_bird_vertices(b)
            draw_bird(v)



        pygame.display.flip()






if __name__ == "__main__":
    flock = Flock.Flock(100, P3.P3(-75, -75, 0), 10)
    f = Render(flock)

    for num in range(10):
        Buildings(random.randrange(-100, 100), random.randrange(-100, 100), random.randrange(1, 10), random.randrange(1, 10), random.randrange(1, 10), (random.randrange(0,2), random.randrange(0,2), random.randrange(0,2)))

    start(0, 0, 800, 600, 1000)


    while 1:
        f.draw()
        for b in flock.boids:
            b.move_Boid(.1)

