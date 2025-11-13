# https://github.com/DRW2007/lab11-DW-JB.git
# Partner 1: Daniel Wagner
# Partner 2: Jacobo Belilty
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5,3), 8)
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(5,0), 5)

    def test_subtract(self): # 3 assertions 
        self.assertEqual(subtract(5,3), 2)
        self.assertEqual(subtract(0,0), 0)
        self.assertEqual(subtract(5,0), 5)
    

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 2), 4)
        self.assertEqual(mul(10, 10), 100)
        self.assertEqual(mul(15, 3), 45)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 10), 1)
        self.assertEqual(div(1, 16), 16)
        self.assertEqual(div(2, 30), 15)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
         self.assertRaises(div(0,10), ZeroDivisionError)
    

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10,10), 1)
        self.assertEqual(logarithm(10,100), 2)
        self.assertEqual(logarithm(10,1000), 3)

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(logarithm(0,10), ValueError)
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        self.assertRaises(logarithm(10, -1), ValueError)

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