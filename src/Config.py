
import json
import P3


class Config_World(object):

    instance = 2

    def __init__(self,objects,flocks,behaviors,screen=None):
        self.screen=screen
        self.objects=objects
        self.flocks=flocks
        self.behaviors=behaviors

    def to_dict(self):

        l_objects = []
        l_flocks = []
        l_behaviors = []

        if self.objects != None:
            for key in self.objects:
                l_objects.append(self.objects[key].to_dict())

        if self.flocks != None:
            for key in self.flocks:
                l_flocks.append(self.flocks[key].to_dict())

        if self.behaviors != None:
            for key in self.behaviors:
                l_behaviors.append(self.behaviors[key].to_dict())

        return dict(objects=l_objects,flocks=l_flocks,behaviors=l_behaviors)

    @staticmethod
    def from_dict(dict):

        l_objects = dict['objects']
        l_flocks = dict['flocks']
        l_behaviors = dict['behaviors']

        d_objects = {}
        d_flocks = {}
        d_behaviors = {}

        if l_objects != None:
            for item in l_objects:
                value = Config_Static_Object.from_dict(item)
                d_objects[value.id]=value

        if l_flocks != None:
            for item in l_flocks:
                value = Config_Flock.from_dict(item)
                d_flocks[value.id]=value

        if l_behaviors != None:
            for item in l_behaviors:
                value = Config_Behavior.from_dict(item)
                d_behaviors[value.id]=value

        return Config_World(objects=d_objects,flocks=d_flocks,behaviors=d_behaviors)

class Config_Screen(object):
    def __init__(self, x_pos, y_pos, x_size, y_size):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.x_size=x_size
        self.y_size=y_size

class Config_Static_Object(object):

    def __init__(self, id, x = 0, y = 0, height = 0, width = 0):
        self.id=id
        self.x=x
        self.y=y
        self.height=height
        self.width=width

    def to_dict(self):
        return dict(id=self.id,x=self.x,y=self.y,height=self.height,width=self.width)

    @staticmethod
    def from_dict(dict):
        if dict!=None:
            return Config_Static_Object(
                dict['id'],
                dict['x'],
                dict['y'],
                dict['height'],
                dict['width']
            )

class Config_Flock(object):

    def __init__(self, id, boids = None, count = 20, behavior_id = 0, center = P3.P3(-100,-100,10), radius = 15):
        self.id = id
        self.boids = boids
        self.count = count
        self.behavior_id = behavior_id
        self.center = center
        self.radius = radius

    def to_dict(self):

        if self.center!=None:
            center = self.center.to_dict()
        else:
            center = None

        return dict(id=self.id,boids=self.boids,count=self.count,behavior_id=self.behavior_id,center=center,radius=self.radius)

    @staticmethod
    def from_dict(dict):
        value = Config_Flock(dict['id'])

        value.boids=dict['boids']
        value.count=dict['count']
        value.behavior_id = dict['behavior_id']

        value.center = P3.P3.from_dict(dict['center'])
        value.radius = dict['radius']

        return value

class Config_Boids(object):

    def __init__(self,count,behavior):
        self.count=count
        self.behavior=behavior

class Config_Boid(object):

    behaviors = ()

    def __init__(self, parent, id, velocity_max, behavior_id, position=None, velocity=None):
        self.parent = parent
        self.id = id
        self.velocity=velocity
        self.position = position
        self.velocity_max=velocity_max
        self.behavior_id = behavior_id

class Config_Behavior(object):

    def __init__(self, id, neighbor = 0, center = 0, direction = 0):
        self.id = id
        self.neighbor_weight = neighbor
        self.center_weight = center
        self.direction_weight = direction

    def to_dict(self):
        return dict(id=self.id,neighbor_weight=self.neighbor_weight,center_weight=self.center_weight,direction_weight=self.direction_weight)

    @staticmethod
    def from_dict(dict):
        return Config_Behavior(dict['id'],dict['neighbor_weight'],dict['center_weight'],dict['direction_weight'])