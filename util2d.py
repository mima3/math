"""平面図形の描画に使用するUtility
"""
import numpy as np
import matplotlib.pyplot as plt
import math


class PolyBuilder:
    """任意の点をユーザが指定してポリゴンを作成する
    """
    def __init__(self, ax, count, callback):
        self.ax = ax
        self.callback = callback
        self.line, = self.ax.plot([], [])  # empty line
        self.scatter = self.ax.scatter([], [])
        self.points = np.array([])
        self.count = count
        self.cid = self.line.figure.canvas.mpl_connect('button_press_event', self)
        self.items = []

    def __call__(self, event):
        if event.inaxes!=self.line.axes: return
        click_point = [math.floor(event.xdata), math.floor(event.ydata)]
        if len(self.points) == 0:
            # 描画された図形があったら削除
            for i in self.items:
                i.remove()
            # ポリゴンの座標を初期化
            self.points = np.array([click_point])
        else:
            self.points = np.vstack((self.points, click_point))
        self.scatter.remove()
        self.scatter = self.ax.scatter(self.points[:,0], self.points[:,1], color='red')
        line_x = self.points[:,0]
        line_y = self.points[:,1]

        if len(self.points) != self.count:
            self.line.set_data(line_x, line_y)
            self.line.figure.canvas.draw()
            return

        # ポリゴン作成
        self.items = self.callback(self.ax, self.points)
        line_x = np.append(line_x, self.points[0,0])
        line_y = np.append(line_y, self.points[0,1])
        self.line.set_data(line_x, line_y)
        self.line.figure.canvas.draw()
        self.points = np.array([])


def get_slope_intercept(x1, y1, x2, y2):
    """2点より傾きと切片を求める
    """
    if x1 == x2:
        return None, None
    a = (y2 - y1)/(x2 - x1)
    b = (a * -1 * x1) + y1
    return a, b


def is_triangle(data):
    """指定の点が三角形の条件を満たしているかチェックする"""
    a = np.linalg.norm(data[1]-data[2])
    b = np.linalg.norm(data[0]-data[2])
    c = np.linalg.norm(data[0]-data[1])
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False
