import unittest

from egzamin import target_practice


class TaskATests(unittest.TestCase):

    def test_1(self):
        self.assertEquals(target_practice("X..........................X.......X..........X......................X..X..........................X"),17)

    def test_2(self):
        self.assertEquals(target_practice("...................................................................................................."),0)

    def test_3(self):
        self.assertEquals(target_practice("............................................X......................................................."),5)

    def test_4(self):
        self.assertEquals(target_practice("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"),220)


if __name__ == '__main__':
    unittest.main()