import typing as tp
import tkinter as tk

from masq import const


def index2binary(index: int):
    return str(bin(index).replace("0b", "")).zfill(4)


def binary2index(b: str):
    return int(b, 2)


"""
point index
3-6-2
7-8-5
0-4-1
"""


def interpolation(v1, v2, v):
    if v1 > v2:
        v_max = v1
        v_min = v2
        left_right = False
    elif v2 > v1:
        left_right = True
        v_max = v2
        v_min = v1
    else:
        raise ValueError(f"v1 == v2, {v1}, {v2}")
    if v < v_min or v > v_max:
        raise ValueError(f"interpolation err: v1={v1}, v2={v2}, v={v}")
    ratio = (v - v_min) / (v_max - v_min)
    if not left_right:
        ratio = 1 - ratio
    return ratio


def index2pos(
        index: int,
        base: tp.Tuple[float, float],
        corner_values: tp.Tuple[float, float, float, float],
        interpolate_value: float,
) -> tp.Tuple[float, float]:
    h = base[0]
    w = base[1]
    if index == 0:
        h += const.UNIT
    elif index == 1:
        h += const.UNIT
        w += const.UNIT
    elif index == 2:
        w += const.UNIT
    elif index == 3:
        pass
    elif index == 4:
        c1 = corner_values[0]
        c2 = corner_values[1]
        ratio = interpolation(c1, c2, interpolate_value)
        w += ratio * const.UNIT
        h += const.UNIT
    elif index == 5:
        c1 = corner_values[2]
        c2 = corner_values[1]
        ratio = interpolation(c1, c2, interpolate_value)
        h += ratio * const.UNIT
        w += const.UNIT
    elif index == 6:
        c1 = corner_values[3]
        c2 = corner_values[2]
        ratio = interpolation(c1, c2, interpolate_value)
        w += ratio * const.UNIT
    elif index == 7:
        c1 = corner_values[3]
        c2 = corner_values[0]
        ratio = interpolation(c1, c2, interpolate_value)
        h += ratio * const.UNIT
    elif index == 8:
        _, w = index2pos(6, base, corner_values, interpolate_value)
        h, _ = index2pos(7, base, corner_values, interpolate_value)
    else:
        raise ValueError(f"index={index} wrong")
    return h, w


class Contour:
    def __init__(
            self, canvas: tk.Canvas,
            left_top_points: tp.Tuple[float, float],
            color="gray80",
            pattern="normal",
    ):
        self.canvas: tk.Canvas = canvas
        self.case_list = const.PATTERNS[pattern]
        self.color = color
        self.left_top_points = left_top_points
        self.id = None

    def remove(self):
        self.canvas.delete(self.id)

    def draw(
            self,
            case: str,
            corner_values: tp.Tuple[float, float, float, float],
            interpolate_value: float,
    ):
        case_index = binary2index(case)
        case = self.case_list[case_index]
        points = []
        for i in case:
            h, w = index2pos(i, self.left_top_points, corner_values, interpolate_value)
            points.extend([w, h])  # convert to x y
        if self.id is not None:
            self.canvas.coords(self.id, *points)
        else:
            self.id = self.canvas.create_polygon(*points, fill=self.color, smooth=0)
            self.canvas.tag_lower(self.id)
