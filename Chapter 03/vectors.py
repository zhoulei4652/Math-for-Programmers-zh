from math import sqrt, sin, cos, acos, atan2

# def add(v1,v2):
#     return (v1[0] + v2[0], v1[1] + v2[1])



# def add(*vectors):
#     by_coordinate = zip(*vectors)
#     coordinate_sums = [sum(coords) for coords in by_coordinate]
#     return tuple(coordinate_sums)

def add(*vectors):
    return tuple(map(sum,zip(*vectors)))
    
def subtract(v1,v2):
    return tuple(v1-v2 for (v1,v2) in zip(v1,v2))

def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))

def dot(u,v):
    return sum([coord1 * coord2 for coord1,coord2 in zip(u,v)])

def distance(v1,v2):
    return length(subtract(v1,v2))

def perimeter(vectors):
    distances = [distance(vectors[i], vectors[(i+1)%len(vectors)])
                    for i in range(0,len(vectors))]
    return sum(distances)

def scale(scalar,v):
    return tuple(scalar * coord for coord in v)

def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length*cos(angle), length*sin(angle))

def rotate(angle, vectors):
    polars = [to_polar(v) for v in vectors]
    return [to_cartesian((l, a+angle)) for l,a in polars]

def translate(translation, vectors):
    return [add(translation, v) for v in vectors]

def to_polar(vector):
    x, y = vector[0], vector[1]
    angle = atan2(y,x)
    return (length(vector), angle)

def angle_between(v1,v2):
    return acos(
                dot(v1,v2) /
                (length(v1) * length(v2))
            )

def cross(u, v):
    ux,uy,uz = u
    vx,vy,vz = v
    return (uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)

def component(v,direction):
    """
    计算向量v在给定方向上的分量

    数学原理：
    向量v在方向direction上的分量可以通过点积计算得出：
    component = (v · direction) / |direction|
    点积的几何意义：
        ①.两个向量的点积：v · direction = |v| * |direction| * cos(θ)
        ②.其中 θ 是两个向量之间的夹角
    推导过程：
        ①.将点积公式代入分量计算公式：cos(θ) = (v · direction) / (|v| * |direction|)
        ②.向量 v 在 direction 方向上的投影长度（带符号）为：投影长度 = |v| * cos(θ)
        ③.将 cos(θ) 的表达式代入投影长度公式，得到：投影长度 = (v · direction) / |direction|
    其中，v · direction表示向量v与方向direction的点积，|direction|表示方向direction的长度（模）。
    这个公式的意义在于，点积反映了两个向量在同一方向上的投影，而除以方向的长度则将这个投影归一化，得到在该方向上的实际分量大小。
    该分量表示了向量v在指定方向上的投影长度，反映了v在该方向上的影响力或贡献度。
    通过这个计算，我们可以了解向量v在特定方向上的表现，从而在物理学、工程学等领域中应用这一概念进行分析和计算。
    """
    return (dot(v,direction) / length(direction))

def unit(v):
    return scale(1./length(v), v)
