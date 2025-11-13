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
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)
    

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10,10), 1.0)
        self.assertAlmostEqual(logarithm(10,100), 2.0)
        self.assertAlmostEqual(logarithm(10,1000), 3.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, -1)


    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(4, 3), 5)
        self.assertAlmostEqual(hypotenuse(6, 8), 10)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(16), 4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()