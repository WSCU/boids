from OpenGL.GL import *

building_vertices = (
    (0,0,0),#0
    (1,0,0),#1
    (1,0,-1),#2
    (0,0,-1),#3
    (0,1,0),#4
    (1,1,0),#5
    (1,1,-1),#6
    (0,1,-1)#7
    )

#call to create a new building
class Buildings(object):
    registry = []

    def __init__(self, x, y, width, height, depth, color):
        self.registry.append(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.depth = depth
        self.color = color

    #sets building verts (render use only)
    def set_building(self):
        new_vertices = []
        final_vertices = []
        global building_count

        #scaling
        for nvert in building_vertices:
            fnew_vert = []

            newv_x = nvert[0] * self.width
            newv_y = nvert[1] * self.depth
            newv_z = nvert[2] * self.height

            fnew_vert.append(newv_x)
            fnew_vert.append(newv_y)
            fnew_vert.append(newv_z)

            new_vertices.append(fnew_vert)

        #positoning
        for vert in new_vertices:
            new_vert = []

            new_x = vert[0] + self.x
            new_y = vert[1] + self.y
            new_z = vert[2]

            new_vert.append(new_x)
            new_vert.append(new_y)
            new_vert.append(new_z)

            final_vertices.append(new_vert)

        return final_vertices

    #displays buildings (render use only)
    def draw_building(self):
        edges = (
        (0, 1),
        (0, 4),
        (1, 2),
        (1, 5),
        (2, 3),
        (2, 6),
        (3, 0),
        (3, 7),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4)
        )
        surfaces = (
            (0,1,2,3),
            (2,6,5,1),
            (0,1,4,5),
            (0,3,7,4),
            (3,7,6,2),
            (7,4,5,6)
        )
        vertices = Buildings.set_building(self)
        glBegin(GL_QUADS)
        for surface in surfaces:
            for vertex in surface:
                glColor3fv(self.color)
                glVertex3fv(vertices[vertex])
        glEnd()


        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glColor3fv((1, 1, 1))
                glVertex3fv(vertices[vertex])
        glEnd()