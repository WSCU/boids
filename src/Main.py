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
Flocks =[]

world = World(guiX,guiY,z,buildings)


def createFlock(size, center, radious):  #adding Flocks to list should be done within the Flock constructor
  F1 = Flock(size, center, radious)
  Flocks.append(F1)

createFlock(5,c,r)

def getFlocks():  #accessing flocks should be done within the flocks class
  return Flocks



def printit():                           #this will be replaced with incremental function calls
  threading.Timer(1.0, printit).start()  #such as flock and boid directional and velocity changes
  print (world.timer.get_time_s())       #instead of displaying time every second

printit()