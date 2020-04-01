import unittest
import bmi

class Testmain(unittest.TestCase):

	def test_calc_bmi(self):
		self.assertEqual(bmi.calculate_bmi(6, 0, 150), 20.83)
		self.assertEqual(bmi.calculate_bmi(5, 3, 125), 22.68)

	def test_get_category(self):
		self.assertEqual(bmi.get_category(18.4), "Underweight")
		self.assertEqual(bmi.get_category(18.5), "Normal weight")
		self.assertEqual(bmi.get_category(24.9), "Normal weight")
		self.assertEqual(bmi.get_category(25), "Overweight")
		self.assertEqual(bmi.get_category(29.9), "Overweight")
		self.assertEqual(bmi.get_category(30), "Obese")

if __name__ == '__main__':
    unittest.main()