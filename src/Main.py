#world_01
import WorldObjects
from World import World
import threading

guiX = 40
guiY = 40
z = 40
buildings = {}

world = World(guiX,guiY,z,buildings)
f1 = Flock(5, )

def printit():                           #this will be replaced with incremental function calls
  threading.Timer(1.0, printit).start()  #such as flock and boid directional and velocity changes
  print (world.timer.get_time_s())       #instead of displaying time every second

printit()