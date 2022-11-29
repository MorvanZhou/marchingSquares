from masq.ms import MarchingSquares


def generate(n_row, n_col):
    ms = MarchingSquares(n_row, n_col, pattern="normal")
    ms.draw_grid()
    ms.random_on()
    ms.after(10, ms.propagate)
    ms.mainloop()
