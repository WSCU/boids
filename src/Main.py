#world_01
import WorldObjects
from World import World
import threading
from src.Flock import Flock

guiX = 40
guiY = 40
z = 40
c = 0
r = 0
buildings = {}

world = World(guiX,guiY,z,buildings)

F1 = Flock(5, c, r)

def updateTick():
  threading.Timer(0.05, F1.update).start()
  print (world.timer.get_time_s())

#can change to pass update and tick to render
F1.update(0.05)


def printit():                           #this will be replaced with incremental function calls
  threading.Timer(1.0, printit).start()  #such as flock and boid directional and velocity changes
  print (world.timer.get_time_s())       #instead of displaying time every second

printit()