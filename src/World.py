import Flock
import render
import Timer
import time
import P3
import src.Config as config

class World:

    tick = 200

    def __init__ (self,settings, gui):
        if isinstance(settings, config.Config_World):
            self.settings = settings
        self.gui = gui
        render.start(self.settings.screen.x_size, self.settings.screen.y_size,1000)

    def drawFlocks(self, flocks):
        for b in flocks.boids:
            b.move_Boid(tick)




if __name__ == "__main__":


    timer = Timer.Timer() #used for measuring elapsed time

    tick = 0.05

    F1 = Flock.Flock(100, P3.P3(-20, 0, 0), 20)

    F1_r = render.Render(F1)

    for num in range(10):
        render.Buildings(render.random.randrange(-10, 10), render.random.randrange(-10, 10),render.random.randrange(1, 10), render.random.randrange(1, 10),
                     render.random.randrange(1, 10), (render.random.randrange(0, 2), render.random.randrange(0, 2), render.random.randrange(0, 2)))



    for i in range(7000):
        F1_r.draw()
        for b in F1.boids:
            b.move_Boid(tick)

        print(timer.get_time_s())
        time.sleep(tick * timer.get_time_s()) #keeping even frame rate by multiplying tick by time elapsed during for loop iteration

        timer.restart()


