import typing as tp

import opensimplex
import numpy as np

from masq.point import Point


PointGrid = tp.List[tp.List[Point]]


def random(row, col):
    return np.random.random(size=(row + 1, col + 1))


def simplex_noise(row, col, z=0, wavelength=5):
    row += 1
    col += 1
    ir = np.linspace(0, row / wavelength, num=row, endpoint=True)
    ic = np.linspace(0, col / wavelength, num=col, endpoint=True)
    iz = np.array([z])
    return (opensimplex.noise3array(ic, ir, iz).squeeze(axis=0) + 1) / 2
