import Flock
import render
import Timer
import time
import P3
import Config
import Buildings
import random

class World:

    tick_time = 10
    tick_step = 0.05
    x_location = -200
    y_location = 100

    def __init__ (self,settings, gui):
        if isinstance(settings, Config.Config_World):
            self.settings = settings
            flock = settings.flocks[0]
            if isinstance(flock,Config.Config_Flock):
                F1 = Flock.Flock(flock.count,flock.center,flock.radius)
        self.gui = gui

        if isinstance(settings.screen, Config.Config_Screen):
            render.start(0,self.settings.screen.y_pos, self.settings.screen.x_size, self.settings.screen.y_size,1000)

        self.render = render.Render(F1)

        #creating city blocks
        for b in range (2):
            self.x_location += 150
            self.y_location = 100

            for z in range(4):
                self.y_location -= 20
                #self.x_location += 20

                for i in range(3):
                    self.y_location -= 10
                    self.x_location -= 30
                    self.c = random.randint(0,1)

                    for t in range(3):
                        self.c2 = random.randint(0,1)
                        Buildings.Buildings(self.x_location, self.y_location, 10, random.randrange(20,65), 10, (self.c, 0, self.c2))
                        self.x_location += 10



        gui.set_tick_method(self.tick)
    def key_left(self):
        self.render.key_left()
        return
    def key_right(self):
        self.render.key_right()
        return
    def key_up(self):
        self.render.key_up()
        return
    def key_down(self):
        self.render.key_down()
        return
    def key_zoom_in(self):
        return
    def key_zoom_out(self):
        return

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

