"""
使用sympy进行符号化的极坐标计算
需要先安装：pip install sympy
"""

try:
    import sympy as sp
    from sympy import pi, sqrt, atan2, simplify, N
    
    def symbolic_to_polar(x, y):
        """
        使用sympy计算极坐标，保持符号形式
        """
        r = sqrt(x**2 + y**2)
        theta = atan2(y, x)
        return (simplify(r), simplify(theta))
    
    # 示例
    print("使用sympy的符号计算：")
    print("-" * 25)
    
    # 常见角度的精确值
    test_cases = [
        (1, 0),           # 0
        (0, 1),           # π/2
        (-1, 0),          # π
        (0, -1),          # -π/2
        (1, 1),           # π/4
        (-1, 1),          # 3π/4
        (sp.sqrt(3), 1),  # π/6
        (1, sp.sqrt(3)),  # π/3
    ]
    
    for x, y in test_cases:
        r, theta = symbolic_to_polar(x, y)
        print(f"({x}, {y}) -> (r={r}, θ={theta})")
        
except ImportError:
    print("需要安装sympy: pip install sympy")
    print("sympy可以进行符号计算，保持π的精确表示")