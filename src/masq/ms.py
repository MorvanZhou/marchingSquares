import tkinter as tk
import random
import typing as tp

from masq.point import Point
from masq.contour import Contour
from masq import const


class MarchingSquares(tk.Tk):
    def __init__(self, n_row: int, n_col: int, pattern="normal"):
        super(MarchingSquares, self).__init__()
        self.width = n_col * const.UNIT
        self.height = n_row * const.UNIT
        self.canvas = tk.Canvas(self, bg='white', height=self.height+const.UNIT*0.2, width=self.width+const.UNIT*0.2)
        self.canvas.pack()
        self.n_row = n_row
        self.n_col = n_col
        self.pattern = pattern
        self.points: tp.List[tp.List[Point]] = []
        self.contours: tp.List[tp.List[Contour]] = []

    def draw_grid(self):
        for r in range(self.n_row + 1):
            row = []
            for c in range(self.n_col + 1):
                y = r * const.UNIT + const.UNIT*0.1
                x = c * const.UNIT + const.UNIT*0.1
                p = Point(self.canvas, [x, y])
                row.append(p)
            self.points.append(row)

    def random_on(self):
        for r in range(self.n_row + 1):
            for c in range(self.n_col + 1):
                p = self.points[r][c]
                if random.random() < 0.5:
                    p.turn_on()

    def propagate(self):
        for r in range(self.n_row):
            row = []
            for c in range(self.n_col):
                p0 = self.points[r + 1][c]
                p1 = self.points[r + 1][c + 1]
                p2 = self.points[r][c + 1]
                p3 = self.points[r][c]
                binary = ""
                for p in [p3, p2, p1, p0]:
                    if p.on:
                        v = "1"
                    else:
                        v = "0"
                    binary += v
                row.append(Contour(
                    self.canvas, left_top_points=[
                        c * const.UNIT + const.UNIT*0.1, r * const.UNIT + const.UNIT*0.1
                    ], case=binary, pattern=self.pattern))
            self.contours.append(row)


