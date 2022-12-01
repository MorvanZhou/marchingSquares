import tkinter as tk
from masq import const


class Point:
    def __init__(self, canvas: tk.Canvas, point, show=False):
        self.r, self.c, self.value = point[0], point[1], point[2]
        self.show = show

        # convert to x y
        if show:
            self.canvas: tk.Canvas = canvas
            ox0, oy0 = self.r - const.POINT_RADIUS, self.c - const.POINT_RADIUS
            ox1, oy1 = self.r + const.POINT_RADIUS, self.c + const.POINT_RADIUS
            self.id = canvas.create_oval(oy0, ox0, oy1, ox1, fill=self._gray_value(), width=0, outline="black")

    def remove(self):
        if self.show:
            self.canvas.delete(self.id)

    def _gray_value(self):
        return f"gray{100 - max(min(int(self.value*100), 99), 1)}"

    def change_value(self, v=0.):
        self.value = v
        if self.show:
            self.canvas.itemconfig(self.id, fill=self._gray_value())

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.__repr__()
