import unittest

from solution import open_lock


class KeyLockTest(unittest.TestCase):

    def test_simple(self):
        self.assertEquals(open_lock([1, 1], [2, 2]), 0)

    def test_simple1(self):
        self.assertEquals(open_lock([1, 2], [2, 1]), 0)

    def test_simple2(self):
        self.assertEquals(open_lock([1, 2, 5], [2, 1, 0]), 1)

    def test_simple3(self):
        self.assertEquals(open_lock([1, 2, 5], [2, 1, 0]), 1)

    def test_simple4(self):
        self.assertEquals(open_lock([5, 5, 6], [0, 0, -1]), -1)

    def test_simple5(self):
        self.assertEquals(open_lock([5, 5, 6], [0]), -1)
