import unittest

from masq.contour import index2binary, binary2index


class BinaryTest(unittest.TestCase):
    def test_2binary(self):
        self.assertEqual("0000", index2binary(0))
        self.assertEqual("0001", index2binary(1))
        self.assertEqual("0010", index2binary(2))
        self.assertEqual("0011", index2binary(3))
        self.assertEqual("0100", index2binary(4))
        self.assertEqual("1110", index2binary(14))
        self.assertEqual("1111", index2binary(15))

    def test_2index(self):
        self.assertEqual(0, binary2index("0000"))
        self.assertEqual(1, binary2index("0001"))
        self.assertEqual(3, binary2index("0011"))
        self.assertEqual(14, binary2index("1110"))
        self.assertEqual(15, binary2index("1111"))
