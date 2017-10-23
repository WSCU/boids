import Flock
import render
import Timer
import time
import P3
import Config
import Building
import random

buildings = []


class World:
    tick_time = 10
    tick_step = 0.05
    x_location = -100
    y_location = 90
    c = random.randint(0, 1)
    c2 = random.randint(0, 1)

    def __init__(self, settings, gui):
        if isinstance(settings, Config.Config_World):
            self.settings = settings
            flock = settings.flocks[0]
            if isinstance(flock, Config.Config_Flock):
                F1 = Flock.Flock(flock.count, flock.center, flock.radius)
        self.gui = gui

        self.render = render.Render(F1)

        if isinstance(settings.screen, Config.Config_Screen):
            render.start(self.settings.screen.x_pos, self.settings.screen.y_pos, self.settings.screen.x_size,
                         self.settings.screen.y_size, 1000)

        # creating city grid
        for b in range(2):
            self.x_location += 100
            self.y_location = 90

            for z in range(3):
                self.y_location -= 20
                # self.x_location += 20

                for i in range(2):
                    self.y_location -= 10
                    self.x_location -= 20
                    self.c = random.randint(0, 1)

                    for t in range(2):
                        self.c2 = random.randint(0, 1)
                        b_location = P3.P3(self.x_location, self.y_location, 0)
                        # print(b_location)
                        buildings.extend(
                            [Building.Building(b_location, 10, random.randrange(20, 65), 10, (self.c, 0, self.c2))])
                        self.x_location += 10

        gui.set_tick_method(self.tick)

    def drawFlocks(self):
        self.render.draw()
        for b in self.render.flock.boids:
            b.move_Boid(World.tick_step)

    def tick(self):
        self.drawFlocks()
        return True

    def key_press(self, event):
        self.render.key_press(event)

    def dipose(self):
        self.gui.set_tick_method(None)
        self.render.dispose()
        self.render = None
