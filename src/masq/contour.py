import tkinter as tk
import copy

from masq import const


def index2binary(index: int):
    return str(bin(index).replace("0b", "")).zfill(4)


def binary2index(b: str):
    return int(b, 2)


class Contour:
    def __init__(self, canvas: tk.Canvas, left_top_points: list, case: str, color="gray", pattern="normal"):
        self.canvas: tk.Canvas = canvas
        points = copy.deepcopy(const.PATTERNS[pattern][binary2index(case)])
        for i in range(0, len(points), 2):
            points[i] = left_top_points[0] + points[i] * const.UNIT
            points[i + 1] = left_top_points[1] + points[i + 1] * const.UNIT
        self.id = None
        if len(points) != 0:
            self.id = self.canvas.create_polygon(*points, fill=color, smooth=0)
            self.canvas.tag_lower(self.id)

    def remove(self):
        self.canvas.delete(self.id)
