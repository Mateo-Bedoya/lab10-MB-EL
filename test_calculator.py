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
       self.assertEqual((2,3),6)
       self.assertEqual((5,0),0)
       self.assertEqual((-2,4),-8)


    def test_divide(self):
        a = 1 /3
        b = 0.333333
        c = 3 / 4
        d = 0.75# 3 assertions
        self.assertAlmostEqual(a,b)
        self.assertEqual((2,2),1)
        self.assertAlmostEqual(c,d)

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
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
    #     fill in code
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5,12),13)
        self.assertAlmostEqual(hypotenuse(3,2),3.61)
    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-1)
        # Test basic function
        #fill in code
        self.assertAlmostEqual(square_root(4),2)
        self.assertAlmostEqual(square_root(9),3)
        self.assertAlmostEqual(square_root(25),5)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()