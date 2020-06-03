"""ユーザが指定した２点を通る一次方程式を求める
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


def draw_linear_equations(ax, data):
    result = []
    # 2点の座標より傾きと切片を求める
    a,b = util2d.get_slope_intercept(data[0][0],data[0][1],data[1][0],data[1][1])
    label = ""
    if a is None:
        # 傾きが存在しない
        line, = ax.plot([data[0][0], data[1][0]], [MIN_Y, MAX_Y], color='gray', linestyle='dotted')
        label = f"x={data[0][0]}"
    else:
        line = draw_line(ax, a, b)
        if b >= 0:
            label = f"y={a}x+{b}"
        else:
            label = f"y={a}x{b}"
    result.append(line)
    result.append(ax.text(data[0][0], data[0][1], f"({data[0][0]},{data[0][1]})"))
    result.append(ax.text(data[1][0], data[1][1], f"({data[1][0]},{data[1][1]})"))
    label_pt = (data[1]+data[0]) / 2
    result.append(ax.text(label_pt[0], label_pt[1], label))
    return result




plt.figure(figsize=(6,6))
plt.xlim(MIN_X, MAX_X)
plt.ylim(MIN_Y, MAX_Y)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
ax = plt.gca()
ax.set_title('click to 2 points.')
poly = util2d.PolyBuilder(ax, 2, draw_linear_equations)
plt.show()
