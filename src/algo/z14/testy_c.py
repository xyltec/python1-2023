import unittest

from c import gen_new_positions


def equals_any_order(list1: list, list2: list) -> bool:
    return sorted(list1) == sorted(list2)


class TaskCTests(unittest.TestCase):

    def test_1(self):
        pos = (0, 0)
        n_pos = gen_new_positions(pos, (8, 8))
        self.assertTrue(n_pos, [(1,2), (2,1)])

    def test_2(self):
        pos = (1, 1)
        n_pos = gen_new_positions(pos, (8, 8))
        self.assertTrue(n_pos, [(0,3), (2,3), (3,0), (3,2)])

 
if __name__ == '__main__':
    unittest.main()