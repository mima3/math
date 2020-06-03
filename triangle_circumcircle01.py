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
    # 各辺の中点を求める
    m = (data[1] + data[0]) / 2
    n = (data[1] + data[2]) / 2
    l = (data[2] + data[0]) / 2
    
    center_scatter = ax.scatter(
        [m[0], n[0], l[0]],
        [m[1], n[1], l[1]],
    )
    result.append(center_scatter)

    # mを通る 法線
    a1, b1 = get_slope_intercept(data[0][0], data[0][1], data[1][0], data[1][1])
    na1 = -1 / a1
    nb1 = m[1] - (na1 * m[0])
    result.append(draw_line(ax, na1, nb1))

    # nを通る 法線
    a2, b2 = get_slope_intercept(data[1][0], data[1][1], data[2][0], data[2][1])
    na2 = -1 / a2
    nb2 = n[1] - (na2 * n[0])
    result.append(draw_line(ax, na2, nb2))

    # lを通る 法線
    a3, b3 = get_slope_intercept(data[2][0], data[2][1], data[0][0], data[0][1])
    na3 = -1 / a3
    nb3 = l[1] - (na3 * l[0])
    result.append(draw_line(ax, na3, nb3))

    # mを通る法線とnを通る法線の交点を求める→外接円の中心となる
    le_l = np.array([
        [na1, -1],
        [na2, -1]
    ])
    le_r = np.array([-1*nb1, -1 * nb2])
    center = np.linalg.solve(le_l,le_r)

    # 半径の取得:円の中心～任意の三角形の頂点の距離
    r = np.linalg.norm(center-data[0])

    # 外接円の描画
    circle = patches.Circle(xy=center, radius=r , facecolor="none", edgecolor='blue')
    ax.add_patch(circle)
    result.append(circle)
    return result




plt.figure(figsize=(6,6))
plt.xlim(MIN_X, MAX_X)
plt.ylim(MIN_Y, MAX_Y)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
ax = plt.gca()
ax.set_title('click to build triangle')
poly = util2d.PolyBuilder(ax, 3, draw_circumcircle)
plt.show()
