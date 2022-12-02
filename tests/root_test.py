import unittest


from masq import noise, marching_squares


class MasqTest(unittest.TestCase):
    def test_tk(self):
        z = [0]
        n_row, n_col = 10, 10
        wavelength = 4
        bound = 0.5
        show_point = True
        increment = 0.1

        def loop():
            while True:
                matrix = noise.simplex_noise(n_row, n_col, z=z[0], wavelength=wavelength)
                ms.draw(matrix, bound=bound, show_point=show_point)
                z[0] += increment

        ms = marching_squares.MarchingSquares(unit=None, pattern="normal")
        ms.after(1, loop)
        ms.after(10, ms.destroy())
        ms.mainloop()
