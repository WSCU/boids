import Flock
import render
import Timer
import time
import P3
import Config

class World:

    tick_time = 10
    tick_step = 0.05

    def __init__ (self,settings, gui):
        if isinstance(settings, Config.Config_World):
            self.settings = settings
            flock = settings.flocks[0]
            if isinstance(flock,Config.Config_Flock):
                F1 = Flock.Flock(flock.count,flock.center,flock.radius)
        self.gui = gui

        if isinstance(settings.screen, Config.Config_Screen):
            render.start(0,self.settings.screen.y_pos, self.settings.screen.x_size, self.settings.screen.y_size,1000)


        #F1 = Flock.Flock(10, P3.P3(-20, 0, 0), 20)
        self.render = render.Render(F1)

        for num in range(10):
            render.Buildings(render.random.randrange(-10, 10), render.random.randrange(-10, 10),
                             render.random.randrange(1, 10), render.random.randrange(1, 10),
                             render.random.randrange(1, 10), (
                             render.random.randrange(0, 2), render.random.randrange(0, 2),
                             render.random.randrange(0, 2)))

        gui.set_tick_method(self.tick)

    def drawFlocks(self):
        self.render.draw()
        for b in self.render.flock.boids:
            b.move_Boid(World.tick_step)

    def tick(self):
        self.drawFlocks()
        return True

"""
    timer = Timer.Timer() #used for measuring elapsed time

    timer.restart()
"""

