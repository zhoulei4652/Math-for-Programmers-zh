from draw3d import *
from vectors import *
from draw2d import *
import matplotlib

octahedron = [
    [(1,0,0), (0,1,0), (0,0,1)],
    [(1,0,0), (0,0,-1), (0,1,0)],
    [(1,0,0), (0,0,1), (0,-1,0)],
    [(1,0,0), (0,-1,0), (0,0,-1)],
    [(-1,0,0), (0,0,1), (0,1,0)],
    [(-1,0,0), (0,1,0), (0,0,-1)],
    [(-1,0,0), (0,-1,0), (0,0,1)],
    [(-1,0,0), (0,0,-1), (0,-1,0)],
]

def vertices(faces):
    return list(set([vertex for face in faces for vertex in face]))

def component(v,direction):
    return (dot(v,direction) / length(direction))

def vector_to_2d(v):
    return (component(v,(1,0,0)), component(v,(0,1,0)))

def face_to_2d(face):
    return [vector_to_2d(vertex) for vertex in face]

blues = matplotlib.colormaps.get_cmap('Blues')

def unit(v):
    return scale(1./length(v), v)

def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

def render(faces, light=(1,2,3), color_map=blues, lines=None):
    polygons = []
    for face in faces:
        # 对于每个面，计算一个长度为1、垂直于当前面的向量
        unit_normal = unit(normal(face)) #1
        print(face,"------>",unit_normal)
        if unit_normal[2] > 0: #2 如果法向量的z分量大于0  说明这个面朝向观察者，需要绘制 否则，这个面背对观察者，不绘制
            c = color_map(1 - dot(unit(normal(face)), unit(light))) #3
            p = Polygon2D(*face_to_2d(face), fill=c, color=lines) #4
            polygons.append(p)
    draw2d(*polygons,axes=False, origin=False, grid=None)

render(octahedron, color_map=matplotlib.colormaps.get_cmap('Blues'), lines=black)