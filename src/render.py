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
bird_velocity_dict = {}

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


#draws the ground (render use only)
def ground():
    glBegin(GL_QUADS)
    for verts in ground_vertices:
        glColor3fv((0,.5,.5))
        glVertex3fv(verts)
    glEnd()


#moves bird according to velocity (render use only)
def update_birds(birdNum):
    thisVelocity = bird_velocity_dict[birdNum]
    thisBird = bird_dict[birdNum]

    #changes the position of the birds vertices
    for vert in thisBird:
        vert[0] = vert[0] + thisVelocity[0] #x value
        vert[1] = vert[1] + thisVelocity[1] #y value
        vert[2] = vert[2] + thisVelocity[2] #z value

    bird_dict[birdNum] = thisBird


#used to display birds (render use only)
def bird(vertices):
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


#sets bird velocity (call to set and change velocity)
def bird_velocity(x_velocity, y_velocity, z_velocity, birdNum):
    bird_velocity_dict[birdNum] = [x_velocity, y_velocity, z_velocity]


#initializes birds at a given x, y, z (call to place birds)
def set_bird_vertices(x, y, z, birdNum = None):
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


#initiates display window (call one time to start display)
def start(width, hieght, depth):
    pygame.init()
    display = (width, hieght)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


    gluPerspective(45, (display[0]/display[1]), 0.1, depth)

    glTranslatef(0, 0, 0)

    glRotatef(0, 0, 0, 0)


#draws objects on screen (call each tick of the clock)
def draw():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    ground()

    for each_bird in bird_velocity_dict:
        update_birds(each_bird)

    for each_bird in bird_dict:
        bird(bird_dict[each_bird])

    pygame.display.flip()




if __name__ == "__main__":
    for num in range(100):
        set_bird_vertices(random.randrange(-20, 20), random.randrange(0, 20), random.randrange(-100, 0))
    start(800, 600, 150)
    for num in range(100):
        bird_velocity(random.randrange(-5, 5), random.randrange(-5, 5), random.randrange(-5, 5), num)
    while True:
        draw()

