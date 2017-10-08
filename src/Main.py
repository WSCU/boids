from src.Flock import Flock
from src.render import Render
import render
import time
import P3

guiX = 40
guiY = 40
z = 40
c = 0
r = 0
buildings = {}
tick = 0.005

F1 = Flock(50, P3.P3(-20, 0, 0), 20)
render.start(800, 600, 1000)

F1_r = Render(F1)

for i in range(7000):
    F1_r.draw()
    for b in F1.boids:  #move all boidds in flock
        b.move_Boid(0.1)

    time.sleep(tick) #wait for length of tick



