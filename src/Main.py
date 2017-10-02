#world_01
from src.WorldObjects import  Buildings
from src.World import World
import threading
from src.Flock import Flock
import render

guiX = 40
guiY = 40
z = 40
buildings = {}
c =0
r=0

world = World(guiX,guiY,z,buildings)
f1 = Flock(5, c, r )

render.get_Flock(f1)

def printit():                           #this will be replaced with incremental function calls
  threading.Timer(1.0, printit).start()  #such as flock and boid directional and velocity changes
  print (world.timer.get_time_s())       #instead of displaying time every second

printit()