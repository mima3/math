"""ユーザが作成した三角形の内接円を作成する
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


def draw_line(ax, a,b):
    x = np.linspace(MIN_X, MAX_X, 100)
    y = np.apply_along_axis(lambda i:i * a + b, 0, [x])
    line, = ax.plot(x, y[0, :], color='gray', linestyle='dotted')
    return line


def draw_incircle(ax, data):
    result = []
    if not util2d.is_triangle(data):
        print("三角形ではありません.")
        print(data)
        return []
    a = np.linalg.norm(data[1]-data[2])
    b = np.linalg.norm(data[0]-data[2])
    c = np.linalg.norm(data[0]-data[1])
    center = [
        (a * data[0][0] + b * data[1][0] + c * data[2][0]) / (a + b + c),
        (a * data[0][1] + b * data[1][1] + c * data[2][1]) / (a + b + c),
    ]
    # 半周長
    s = (a + b + c) / 2
    # 内接円の半径
    r = (((s-a) * (s-b) * (s-c)) / s) ** 0.5
    circle = patches.Circle(xy=center, radius=r , facecolor="none", edgecolor='blue')
    ax.add_patch(circle)
    result.append(circle)

    return result




plt.figure(figsize=(5,5))
plt.xlim(MIN_X, MAX_X)
plt.ylim(MIN_Y, MAX_Y)
ax = plt.gca()
ax.set_title('click to build triangle')
poly = util2d.PolyBuilder(ax, 3, draw_incircle)
plt.show()
