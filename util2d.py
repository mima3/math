"""平面図形の描画に使用するUtility
"""
import numpy as np
import matplotlib.pyplot as plt


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
        if len(self.points) == 0:
            # 描画された図形があったら削除
            for i in self.items:
                i.remove()
            # ポリゴンの座標を初期化
            self.points = np.array([[event.xdata, event.ydata]])
        else:
            self.points = np.vstack((self.points, [event.xdata, event.ydata]))
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
