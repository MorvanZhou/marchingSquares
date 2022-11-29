import tkinter as tk
from masq import const

POINT_RADIUS = const.UNIT * 0.05


class Point:
    def __init__(self, canvas: tk.Canvas, point):
        self.canvas: tk.Canvas = canvas
        self.x, self.y = point[0], point[1]
        ox0, oy0 = self.x - POINT_RADIUS, self.y - POINT_RADIUS
        ox1, oy1 = self.x + POINT_RADIUS, self.y + POINT_RADIUS
        self.id = canvas.create_oval(ox0, oy0, ox1, oy1, fill="white", width=1, outline="black")
        self.on = False

    def move(self, x, y):
        self.canvas.coords(
            self.id,
            x - POINT_RADIUS, y - POINT_RADIUS,
            x + POINT_RADIUS, y + POINT_RADIUS,
        )

    def remove(self):
        self.canvas.delete(self.id)

    def turn_on(self):
        self.on = True
        self.canvas.itemconfig(self.id, fill="black")

    def turn_off(self):
        self.on = False
        self.canvas.itemconfig(self.id, fill="white")

    def __repr__(self):
        return "o" if self.on else "x"

    def __str__(self):
        return self.__repr__()
