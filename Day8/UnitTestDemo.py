import unittest
from doctest_demo import Division 

class TestDivMethods(unittest.TestCase):
    def test_div_asserts_proper_value(self):
        self.assertEqual(Division(8,4), 2.0)

    def test_div_asserts_zero(self):
        self.assertEqual(Division(0,4), 0.0)

    def test_div_negative(self):
        self.assertEqual(Division(9,3), 5)

    def test_div_asserts_one(self):
        self.assertEqual(Division(3,3), 1)    


if __name__ == '__main__':
    unittest.main()