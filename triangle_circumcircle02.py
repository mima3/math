"""ユーザが作成した三角形の外接円の作成する
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as patches
import util2d

MAX_X = 100.0
MIN_X = -100.0
MAX_Y = 100.0
MIN_Y = -100.0

def get_slope_intercept(x1, y1, x2, y2):
    a = (y2 - y1)/(x2 - x1)
    b = (a * -1 * x1) + y1
    return a, b

def draw_line(ax, a,b):
    x = np.linspace(MIN_X, MAX_X, 100)
    y = np.apply_along_axis(lambda i:i * a + b, 0, [x])
    line, = ax.plot(x, y[0, :], color='gray', linestyle='dotted')
    return line


def draw_circumcircle(ax, data):
    result = []
    
    if not util2d.is_triangle(data):
        print("三角形ではありません.")
        print(data)
        return []
    
    a = np.linalg.norm(data[1]-data[2])
    b = np.linalg.norm(data[0]-data[2])
    c = np.linalg.norm(data[0]-data[1])
    
    # 外接円の描画
    # https://ja.wikipedia.org/wiki/%E5%A4%96%E6%8E%A5%E5%86%86
    u = (a**2 * (b**2+c**2-a**2)*data[0] + b**2 * (c**2+a**2-b**2)*data[1] + c**2 * (a**2+b**2-c**2) * data[2]) / (a**2 * (b**2+c**2-a**2) + b**2 * (c**2 +a**2-b**2) + c**2 * (a**2+b**2 - c**2))
    r = (a*b*c) / np.sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))
    circle = patches.Circle(xy=u, radius=r , facecolor="none", edgecolor='blue')
    ax.add_patch(circle)
    result.append(circle)
    return result




plt.figure(figsize=(5,5))
plt.xlim(MIN_X, MAX_X)
plt.ylim(MIN_Y, MAX_Y)
plt.grid(b=True, which='major', color='#666666', linestyle='-')

ax = plt.gca()
ax.set_title('click to build triangle')
poly = util2d.PolyBuilder(ax, 3, draw_circumcircle)
plt.show()
