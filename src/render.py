import pygame
from pygame import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import Flock
import Boid
import P3

x = 800
y = 600
z = 1000

bird_count = 0
bird_dict = {}
bird_velocity_dict = {}
building_dict = {}
building_count = 0
color_list = []
boid_dict = {}

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


#draws the ground (render use only)
def ground():
    glBegin(GL_QUADS)
    for edges in ground_edges:
        for vert in edges:
            glColor3fv((0,.5,.5))
            glVertex3fv(ground_vertices[vert])
    glEnd()


#moves bird according to velocity (render use only)
def update_birds(birdNum):
    thisVelocity = bird_velocity_dict[birdNum]
    thisBird = bird_dict[birdNum]
    #print(thisBird)
    #changes the position of the birds vertices
    for vert in thisBird:
        vert[0] = vert[0] + thisVelocity[0] #x value
        vert[1] = vert[1] + thisVelocity[1] #y value
        vert[2] = vert[2] + thisVelocity[2] #z value

    bird_dict[birdNum] = thisBird


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


#sets bird velocity (call to set and change velocity)
#birdNum = 0 -> (# of birds added - 1)
def bird_velocity(x_velocity, y_velocity, z_velocity, birdNum):
    bird_velocity_dict[birdNum] = [x_velocity, y_velocity, z_velocity]

def building(vertices, color):
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
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv(color)
            glVertex3fv(vertices[vertex])
    glEnd()


    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1, 1, 1))
            glVertex3fv(vertices[vertex])
    glEnd()


def set_building(bx, by, bz, width, height, depth):
    new_vertices = []
    final_vertices = []
    global building_count

    #positoning
    for vert in building_vertices:
        new_vert = []

        new_x = vert[0] + bx
        new_y = vert[1] + by
        new_z = vert[2] + bz

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    #scaling
    for nvert in new_vertices:
        fnew_vert = []

        newv_x = nvert[0] * width
        newv_y = nvert[1] * depth
        newv_z = nvert[2] * height

        fnew_vert.append(newv_x)
        fnew_vert.append(newv_y)
        fnew_vert.append(newv_z)

        final_vertices.append(fnew_vert)

    building_dict[building_count] = final_vertices
    building_count += 1
    color_list.append(color)


#initializes birds at a given x, y, z (call add a bird)
def make_bird_vertices(bird):
    new_vertices = []
    global bird_count

    for vert in bird_vertices:
        new_vert = []

        new_x = vert[0] + bird.position.x
        new_y = vert[1] + bird.position.y
        new_z = vert[2] + bird.position.z

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        # new_vertices.append(new_vert)
        new_vertices.append(new_vert)


    #bird_dict[bird_count] = new_vertices
    #bird_count += 1
    return new_vertices


#initiates display window (call one time to start display)
def start(width, hieght, depth):
    pygame.init()
    display = (width, hieght)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, depth)
    glTranslatef(-10, 30, -250)
    glRotatef(-45, 1, 1, 1)


#draws objects on screen (call each tick of the clock)
def draw():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


    ground()

    # for each_bird in bird_velocity_dict:
    #     update_birds(each_bird)
    #
    # for each_bird in bird_dict:
    #     bird(bird_dict[each_bird])
    #
    for each_building in building_dict:
        building(building_dict[each_building], color_list[each_building])

    for b in flock.boids:
        v = make_bird_vertices(b)
        draw_bird(v)



    pygame.display.flip()






if __name__ == "__main__":
    #for num in range(100):
        #set_bird_vertices(random.randrange(-20, 20), random.randrange(0, 20), random.randrange(-100, 0))
    flock = Flock.Flock(100, P3.P3(-20, 0, 0), 20)
    # for b in flock.boids:
    start(800, 600, 1000)

    for num in range(10):
        color = (random.randrange(0, 2), random.randrange(0, 2), random.randrange(0, 2))
        color_list.append(color)

    for num in range(10):
        set_building(random.randrange(-10,10), random.randrange(-10,10), 0,random.randrange(2,20) , random.randrange(2,20), random.randrange(2,20))

    while 1:
        draw()
        for b in flock.boids:
            b.move_Boid(.1)
        #make_bird_vertices(flock.boids[i])
        #bird_velocity(flock.boids[i].vel.x, flock.boids[i].vel.y, flock.boids[i].vel.z, i)


    # for num in range(100):
    #     bird_velocity(random.randrange(-5, 5), random.randrange(-5, 5), random.randrange(-5, 5), num)






