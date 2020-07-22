import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_3_6_returns_3_is_less_than_6(self):
        self.assertEqual("3 is less than 6", compare(3, 6))