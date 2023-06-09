import math
class Calculator: 
  def add(self, a, b):
    return a+b
  def subtract(self, a, b):
    return a-b
  def squareRoot(self, a):
    return math.sqrt(a)
  def multiply(self,a, b):
    return a*b
    
import unittest
#from Calculator import Calculator
class CalculatorTest(unittest.TestCase):
  def setUp(self):
    self.calc = Calculator()
  def test_add(self):
     self.assertEqual(10, self.calc.add(3, 7), "The addition is wrong")
  def test_subtract(self):
    self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is wrong")
  def test_multiply(self):
    self.assertEqual(30, self.calc.multiply(5, 6), "Multiplication is wrong")
 
if __name__ == '__main__':
  unittest.main()