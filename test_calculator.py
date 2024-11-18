import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(0, -1), -1)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(-1, 4), -5)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-9, -2), 18)
        self.assertEqual(self.calc.multiply(4, -2), -8)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 1), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 4), 1)
        self.assertEqual(self.calc.modulo(-1, 5), 4)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()