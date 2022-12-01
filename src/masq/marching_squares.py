import tkinter as tk
import typing as tp

import numpy as np

from masq.point import Point
from masq.contour import Contour
from masq import const


class MarchingSquares(tk.Tk):
    def __init__(self, unit=None, pattern="normal"):
        super(MarchingSquares, self).__init__()
        self.pattern = pattern
        self.canvas = tk.Canvas(self, bg='white', height=0, width=0)
        self.canvas.pack()
        if unit is not None:
            const.set_unit(unit)
        self.points: tp.List[tp.List[Point]] = []
        self.contours: tp.List[tp.List[Contour]] = []
        self.count = 0

    def reset(self, matrix: np.ndarray, row, col, interpolate_value=0.5, show_point=False):
        width = col * const.UNIT
        height = row * const.UNIT
        self.canvas.config(height=height + const.UNIT * 0.2, width=width + const.UNIT * 0.2)

        if len(self.points) != 0:
            for r in range(row + 1):
                for c in range(col + 1):
                    self.points[r][c].change_value(matrix[r][c])
        else:
            for r in range(row + 1):
                new_row = []
                for c in range(col + 1):
                    r_ = r * const.UNIT + const.UNIT * 0.1
                    c_ = c * const.UNIT + const.UNIT * 0.1
                    v = matrix[r][c]
                    p = Point(self.canvas, [r_, c_, v], show_point)
                    new_row.append(p)
                self.points.append(new_row)

        for r in range(row):
            for c in range(col):
                p0 = self.points[r + 1][c]
                p1 = self.points[r + 1][c + 1]
                p2 = self.points[r][c + 1]
                p3 = self.points[r][c]
                binary = ""
                for p in [p3, p2, p1, p0]:
                    if p.value > interpolate_value:
                        v = "1"
                    else:
                        v = "0"
                    binary += v

                try:
                    contour_row = self.contours[r]
                except IndexError:
                    contour_row = []
                    self.contours.append(contour_row)
                try:
                    contour = contour_row[c]
                except IndexError:
                    contour = Contour(
                        self.canvas,
                        left_top_points=(
                            r * const.UNIT + const.UNIT*0.1, c * const.UNIT + const.UNIT*0.1
                        ),
                        pattern=self.pattern
                    )
                    contour_row.append(contour)
                contour.draw(
                    case=binary,
                    corner_values=(p0.value, p1.value, p2.value, p3.value),
                    interpolate_value=interpolate_value,
                )

    def draw(self, matrix: np.ndarray, interpolate_value=0.5, show_point=True):
        n_row = matrix.shape[0] - 1
        n_col = matrix.shape[1] - 1
        self.reset(matrix, n_row, n_col, interpolate_value, show_point)
        self.update()
