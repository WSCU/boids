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

        if isinstance(settings.screen, config.Config_Screen):
            render.start(self.settings.screen.x_size, self.settings.screen.y_size,1000)

        F1 = Flock.Flock(100, P3.P3(-20, 0, 0), 20)
        self.flock = render.Render(F1)

        for num in range(10):
            render.Buildings(render.random.randrange(-10, 10), render.random.randrange(-10, 10),
                             render.random.randrange(1, 10), render.random.randrange(1, 10),
                             render.random.randrange(1, 10), (
                             render.random.randrange(0, 2), render.random.randrange(0, 2),
                             render.random.randrange(0, 2)))

    def drawFlocks(self):
        for b in self.flock.boids:
            b.move_Boid(self.tick)

    def tick(self):
        self.drawFlocks(self.flock)
        return True

"""
    timer = Timer.Timer() #used for measuring elapsed time

    timer.restart()
"""

