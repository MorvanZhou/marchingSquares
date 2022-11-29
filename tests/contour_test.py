import unittest
import tkinter as tk


from masq.contour import Contour


class ContourTest(unittest.TestCase):
    def test_contour(self):
        root = tk.Tk()
        c = tk.Canvas(root, bg='white')
        c.pack()
        Contour(c, [10, 10], case="1111")
        root.mainloop()
