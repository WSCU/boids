import Flock
import render
import Timer
import time
import P3


class World:

    def __init__ (self,screen, objects,flocks):
        self.screen = screen
        self.objects = objects
        self.flocks = flocks

timer = Timer.Timer() #used for measuring elapsed time

tick = 0.05

F1 = Flock.Flock(100, P3.P3(-20, 0, 0), 20)

F1_r = render.Render(F1)

for num in range(10):
    render.Buildings(render.random.randrange(-10, 10), render.random.randrange(-10, 10),render.random.randrange(1, 10), render.random.randrange(1, 10),
                     render.random.randrange(1, 10), (render.random.randrange(0, 2), render.random.randrange(0, 2), render.random.randrange(0, 2)))


render.start(800, 600, 1000)

for i in range(7000):
    F1_r.draw()
    for b in F1.boids:
        b.move_Boid(tick)

    print(timer.get_time_s())
    time.sleep(tick * timer.get_time_s()) #keeping even frame rate by multiplying tick by time elapsed during for loop iteration

    timer.restart()


