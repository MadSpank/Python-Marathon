import unittest


def divide(num_1,num_2):
    return float(num_1)/num_2

class DivideTest(unittest.TestCase):
    
    def test_zero_division(self):

        self.assertNotEqual(ZeroDivisionError, divide, True)
    
    def test_type_error(self):
        self.assertRaises(TypeError, divide, True)
    
    def test_divide(self):
        given = divide(13,3)
        expected =  4.3333333
        self.assertAlmostEqual(given, expected)