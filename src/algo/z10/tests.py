from solution import longest_sequence
import unittest

class SequenceTest(unittest.TestCase):

    def test_1(self):
        self.assertEquals(longest_sequence("><<>><>>><<<","<"),3)
    def test_2(self):
        self.assertEquals(longest_sequence(">><<<><><><><><<<<<","<"),5)
    def test_3(self):
        self.assertEquals(longest_sequence("<<<><><>>><>><><>>>","@"),-1)
    def test_4(self):
        self.assertEquals(longest_sequence(">>><><<<>>>>>>><<<>",">"),7)
    def test_5(self):
        self.assertEquals(longest_sequence("<>ab1<>>cd2<<>>>>efghijk",">"),-1)
    def test_6(self):
        self.assertEquals(longest_sequence("",">"),0)
    def test_7(self):
        self.assertEquals(longest_sequence("<<<<<>>>>><<<<<>>>>>",">"),5)
if __name__ == '__main__':
    unittest.main()