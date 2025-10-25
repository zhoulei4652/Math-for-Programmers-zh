from vectors import to_polar, to_cartesian
from teapot import load_triangles
from draw_model import draw_model
from math import pi
from transforms import *

def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]

def rotate2d(angle, vector):
    # 将传入的笛卡尔左边转换为极坐标
    l,a = to_polar(vector)
    # 加上角度之后，再将旋转之后的极坐标再转换成笛卡尔坐标
    return to_cartesian((l, a+angle))

def rotate_z(angle, vector):
    x,y,z = vector
    new_x, new_y = rotate2d(angle, (x,y))
    return new_x, new_y, z

def rotate_z_by(angle):
    def new_function(v):
        return rotate_z(angle,v)
    return new_function

####################################################################
#### this code takes a snapshot to reproduce the exact figure 
#### shown in the book as an image saved in the "figs" directory
#### to run it, run this script with command line arg --snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig_4.11_rotate_teapot',[0])
####################################################################

draw_model(polygon_map(compose_1(rotate_x_by(pi/2),rotate_z_by(pi/2)), load_triangles()))
