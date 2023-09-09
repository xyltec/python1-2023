import unittest

from a import is_on_board


class TaskATests(unittest.TestCase):

    def test_1(self):
        self.assertTrue(is_on_board((0,0), (8,8)))

    def test_2(self):
        self.assertFalse(is_on_board((0,-1), (8,8)))

    def test_3(self):
        self.assertFalse(is_on_board((0,8), (8,8)))

    def test_4(self):
        self.assertTrue(is_on_board((7, 7), (8,8)))


if __name__ == '__main__':
    unittest.main()