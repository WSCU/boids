import pygame
from pygame import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import Flock
import Boid

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
buidling_vertices = (
    (0,0,1),#0
    (1,0,1),#1
    (0,0,0),#2
    (1,0,0),#3
    (0,1,1),#4
    (1,1,1),#5
    (0,1,0),#6
    (1,1,0)#7
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
    print(thisBird)
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
#birdNum = 0 -> (# of birds added - 1)
def bird_velocity(x_velocity, y_velocity, z_velocity, birdNum):
    bird_velocity_dict[birdNum] = [x_velocity, y_velocity, z_velocity]

def buidling(vertices):
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
    for edge in edges:
        for vertex in edge:
            glColor3fv((1,1,1))
            glVertex3fv(vertices[vertex])
    glEnd()

def set_building(x, y, z, width, height, depth, color):
    new_vertices = []




    return

#initializes birds at a given x, y, z (call add a bird)
def set_bird_vertices(x, y, z):
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

    bird_dict[bird_count] = new_vertices
    bird_count += 1


#initiates display window (call one time to start display)
def start(width, hieght, depth):
    pygame.init()
    display = (width, hieght)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45 , (display[0]/display[1]), 0.1, depth)
    #glTranslatef(0, 0, 0)


#draws objects on screen (call each tick of the clock)
def draw():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    ground()

    for each_bird in bird_velocity_dict:
        update_birds(each_bird)

    for each_bird in bird_dict:
        bird(bird_dict[each_bird])

    pygame.display.flip()




if __name__ == "__main__":
    #for num in range(100):
        #set_bird_vertices(random.randrange(-20, 20), random.randrange(0, 20), random.randrange(-100, 0))
    flock = Flock.Flock(100, 0, 0)
    # for b in flock.boids:
    for i in range(len(flock.boids)):
        set_bird_vertices(flock.boids[i].position.x, flock.boids[i].position.y, flock.boids[i].position.z)
        bird_velocity(flock.boids[i].vel.x, flock.boids[i].vel.y, flock.boids[i].vel.z, i)
    start(800, 600, 150)
    # for num in range(100):
    #     bird_velocity(random.randrange(-5, 5), random.randrange(-5, 5), random.randrange(-5, 5), num)
    while True:
        draw()

