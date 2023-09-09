import unittest

from b import make_move


class TaskATests(unittest.TestCase):

    def test_1(self):
        self.assertEquals(make_move((0,0), (8,8)), (8,8))

    def test_2(self):
        self.assertEquals(make_move((1,3), (2,-1)), (3,2))

    def test_3(self):
        self.assertEquals(make_move((1,2), (3,4)), (4,6))


if __name__ == '__main__':
    unittest.main()