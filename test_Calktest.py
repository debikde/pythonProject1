import unittest
from laba5 import Calculator

class TestCalculator(unittest.TestCase):

  def setUp(self):
    self.calculator = Calculator()

  def test_add(self):
    self.assertEqual(self.calculator.summ(5,5), 1, "ошибка в сумме")
  def test_subtract(self):
    self.assertEqual(self.calculator.minus(10,3), 7, "ошибка в вычитании")
  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(0,7), 0, "ошибка в умножении")
  def test_divide(self):
    self.assertEqual(self.calculator.divide(100,2), 50, "ошибка в делении")

if __name__ == "__main__":
  unittest.main()
