import unittest
from simple_calculator import SimpleCalculator

class TestCalcNumbers(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(3, 7),10)
        self.assertEqual(self.calc.add(2,5), 7)
        self.assertEqual(self.calc.add(4,8), 12)
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,3), 2)
        self.assertEqual(self.calc.subtract(7,5), 2)
        self.assertEqual(self.calc.subtract(10,8), 2)
        
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3,5), 15)
        self.assertEqual(self.calc.multiply(2,7), 14)
        self.assertEqual(self.calc.multiply(4,8), 32)
        
    def test_division(self):
        self.assertEqual(self.calc.divide(10,2), 5)
        self.assertEqual(self.calc.divide(14,7), 2)
        self.assertEqual(self.calc.divide(16,2), 8)
        
if __name__ == "__main__":
    unittest.main()