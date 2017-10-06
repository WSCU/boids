#world_01
import WorldObjects
from World import World
import threading
from src.Flock import Flock
from src.render import Render
import time
import P3

guiX = 40
guiY = 40
z = 40
c = 0
r = 0
buildings = {}
tick = 0.05

world = World(guiX,guiY,z,buildings)

F1 = Flock(100, P3.P3(-20, 0, 0), 20)
F1_r = Render(F1)

for i in range(7000):
  print(tick)
  F1_r.draw()
  time.sleep(tick)


#can change to pass update and tick to render
# F1.update(0.05)

