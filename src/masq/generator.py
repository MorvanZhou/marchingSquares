import time

from masq.marching_squares import MarchingSquares
from masq import noise


def random(n_row, n_col, interpolate_value=0.5, show_point=False, unit=None):
    ms = MarchingSquares(unit=unit, pattern="normal")
    matrix = noise.random(n_row, n_col)
    ms.draw(matrix, interpolate_value=interpolate_value, show_point=show_point)
    ms.mainloop()


def loop_random(n_row, n_col, interpolate_value=0.5, show_point=False, unit=None):
    def loop():
        while True:
            matrix = noise.random(n_row, n_col)
            ms.draw(matrix, interpolate_value=interpolate_value, show_point=show_point)
            time.sleep(0.02)
    ms = MarchingSquares(unit=unit, pattern="normal")
    ms.after(1, loop)
    ms.mainloop()


def simplex_noise(n_row, n_col, interpolate_value=0.5, size=0.8, show_point=False, unit=None):
    ms = MarchingSquares(unit=unit, pattern="normal")
    matrix = noise.simplex_noise(n_row, n_col, z=0, size=size)
    ms.draw(matrix, interpolate_value=interpolate_value, show_point=show_point)
    ms.mainloop()


def loop_simplex_noise(n_row, n_col, interpolate_value=0.5, size=0.8, increment=0.01, show_point=False, unit=None):
    z = [0]

    def loop():
        while True:
            matrix = noise.simplex_noise(n_row, n_col, z=z[0], size=size)
            ms.draw(matrix, interpolate_value=interpolate_value, show_point=show_point)
            z[0] += increment

    ms = MarchingSquares(unit=unit, pattern="normal")
    ms.after(1, loop)
    ms.mainloop()
