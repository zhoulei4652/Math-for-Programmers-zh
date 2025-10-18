from math import pi, sqrt, atan2, gcd
from fractions import Fraction

def format_angle_with_pi(angle):
    """
    将弧度角度格式化为π的形式
    
    angle: 弧度值
    return: 格式化的字符串
    """
    # 将角度除以π
    ratio = angle / pi
    
    # 如果接近0
    if abs(ratio) < 1e-10:
        return "0"
    
    # 如果接近整数倍的π
    if abs(ratio - round(ratio)) < 1e-10:
        n = round(ratio)
        if n == 1:
            return "π"
        elif n == -1:
            return "-π"
        elif n == 0:
            return "0"
        else:
            return f"{n}π"
    
    # 尝试用分数表示，使用更严格的匹配
    frac = Fraction(ratio).limit_denominator(1000)  # 增加精度
    
    # 检查常见的分数值，使用更宽松的容差
    common_fractions = {
        0.25: "π/4", -0.25: "-π/4",
        0.5: "π/2", -0.5: "-π/2", 
        0.75: "3π/4", -0.75: "-3π/4",
        1.25: "5π/4", -1.25: "-5π/4",
        1.5: "3π/2", -1.5: "-3π/2",
        1.75: "7π/4", -1.75: "-7π/4",
        0.125: "π/8", -0.125: "-π/8",
        0.375: "3π/8", -0.375: "-3π/8",
        0.625: "5π/8", -0.625: "-5π/8",
        0.875: "7π/8", -0.875: "-7π/8",
        1.125: "9π/8", -1.125: "-9π/8",
        1.375: "11π/8", -1.375: "-11π/8",
        1.625: "13π/8", -1.625: "-13π/8",
        1.875: "15π/8", -1.875: "-15π/8",
        # 添加更精确的常见值
        1/4: "π/4", -1/4: "-π/4",
        1/2: "π/2", -1/2: "-π/2",
        3/4: "3π/4", -3/4: "-3π/4",
        5/4: "5π/4", -5/4: "-5π/4",
        3/2: "3π/2", -3/2: "-3π/2",
        7/4: "7π/4", -7/4: "-7π/4"
    }
    
    # 检查是否匹配常见分数，使用较宽松的容差
    for decimal_val, pi_str in common_fractions.items():
        if abs(ratio - decimal_val) < 1e-6:  # 放宽容差
            return pi_str
    
    # 使用Fraction进行通用处理
    if abs(float(frac) - ratio) < 1e-10:
        if frac.numerator == 1:
            if frac.denominator == 1:
                return "π"
            else:
                return f"π/{frac.denominator}"
        elif frac.numerator == -1:
            if frac.denominator == 1:
                return "-π"
            else:
                return f"-π/{frac.denominator}"
        else:
            if frac.denominator == 1:
                return f"{frac.numerator}π"
            else:
                return f"{frac.numerator}π/{frac.denominator}"
    
    # 如果无法简化，返回小数形式但避免显示0.xxx
    if abs(ratio) > 1e-6:  # 避免显示很小的数字
        return f"{ratio:.3f}π"
    else:
        return "0"

def format_polar_vector(polar_vector):
    """
    格式化极坐标向量，角度用π表示
    
    polar_vector: (长度, 角度) 的元组
    return: 格式化的字符串
    """
    length, angle = polar_vector
    angle_str = format_angle_with_pi(angle)
    return f"({length:.3f}, {angle_str})"

def format_polar_vector_positive(polar_vector):
    """
    格式化极坐标向量，角度转换为正值并用π表示
    
    polar_vector: (长度, 角度) 的元组
    return: 格式化的字符串
    """
    length, angle = polar_vector
    # 如果角度为负，加上2π使其为正
    if angle < 0:
        angle += 2 * pi
    angle_str = format_angle_with_pi(angle)
    return f"({length:.3f}, {angle_str})"

class PolarVector:
    """
    专为Jupyter设计的极坐标向量类，防止自动计算分数
    """
    def __init__(self, polar_vector, use_positive_angle=True):
        self.length, self.angle = polar_vector
        self.use_positive_angle = use_positive_angle
    
    def __repr__(self):
        if self.use_positive_angle:
            return format_polar_vector_positive((self.length, self.angle))
        else:
            return format_polar_vector((self.length, self.angle))
    
    def __str__(self):
        return self.__repr__()

def polar_display(vector, positive_angle=True):
    """
    返回一个适合在Jupyter中显示的极坐标对象
    
    vector: 笛卡尔坐标 (x, y)
    positive_angle: 是否使用正角度表示
    """
    from vectors import to_polar
    
    # 总是将输入视为笛卡尔坐标进行转换
    polar_vec = to_polar(vector)
    return PolarVector(polar_vec, positive_angle)

def polar_display_from_polar(polar_vector, positive_angle=True):
    """
    直接从极坐标创建显示对象
    
    polar_vector: 极坐标 (r, θ)
    positive_angle: 是否使用正角度表示
    """
    return PolarVector(polar_vector, positive_angle)

# 示例使用
if __name__ == "__main__":
    from vectors import to_polar
    
    # 测试一些常见的点
    test_points = [
        (1, 0),      # 0度
        (0, 1),      # 90度
        (-1, 0),     # 180度  
        (0, -1),     # 270度
        (1, 1),      # 45度
        (-1, 1),     # 135度
        (1, -1),     # -45度 or 315度
        (-1, -1),    # -135度 or 225度
    ]
    
    print("笛卡尔坐标 -> 极坐标（π格式）")
    print("-" * 40)
    for point in test_points:
        polar = to_polar(point)
        formatted_standard = format_polar_vector(polar)
        formatted_positive = format_polar_vector_positive(polar)
        print(f"{point} -> {formatted_standard} 或 {formatted_positive}")
    
    print("\n" + "="*50)
    print("只显示标准角度范围 [-π, π]:")
    print("-" * 40)
    for point in test_points:
        polar = to_polar(point)
        formatted = format_polar_vector(polar)
        print(f"{point} -> {formatted}")
    
    print("\n" + "="*50)
    print("只显示正角度范围 [0, 2π):")
    print("-" * 40)
    for point in test_points:
        polar = to_polar(point)
        formatted = format_polar_vector_positive(polar)
        print(f"{point} -> {formatted}")