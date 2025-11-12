# https://github.com/DRW2007/lab11-DW-JB.git
# Partner 1: Daniel Wagner
# Partner 2: Jacobo Belilty
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 2), 4)
        self.assertEqual(mul(10, 10), 100)
        self.assertEqual(mul(15, 3), 45)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 10), 1)
        self.assertEqual(div(16, 1), 16)
        self.assertEqual(div(30, 2), 15)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        self.assertRaises(log(10, -1), ValueError)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(10, 10), 14.14214)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.41421)
        self.assertAlmostEqual(hypotenuse(5, 3), 5.83095)

    def test_sqrt(self): # 3 assertions
        self.assertRaises(square_root(-1), ValueError)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(16), 4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()