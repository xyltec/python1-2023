import unittest

from solution2 import *


class SemVerTest(unittest.TestCase):

    def test_1(self):
        self.assertEquals(get_latest(['1.0.0', '1.0.5', '1.1.0']), '1.1.0')
        self.assertEquals(get_latest(['1.13.0', '2.0.5', '1.1.7']), '2.0.5')
        self.assertEquals(get_latest(['1.13.0']), '1.13.0')
        self.assertEquals(get_latest(['0.9.9', '1.0.0']), '1.0.0')

    def test_2(self):
        self.assertEquals(next_version('1.0.0', 2), '1.0.1')
        self.assertEquals(next_version('1.0.0', 1), '1.1.0')
        self.assertEquals(next_version('1.0.0', 0), '2.0.0')

    def test_3(self):
        self.assertEquals(next_version('2.21.2', 2), '2.21.3')
        self.assertEquals(next_version('2.21.2', 1), '2.22.0')
        self.assertEquals(next_version('2.21.2', 0), '3.0.0')


if __name__ == '__main__':
    unittest.main()
