import unittest
import retirement


class Testmain(unittest.TestCase):

    def test_calc_bmi(self):
        self.assertEqual(retirement.calculate_retirement(22, 60000, 15, 800000), 88)
        self.assertEqual(retirement.calculate_retirement(30, 100000, 20, 1000000), 68)


if __name__ == '__main__':
    unittest.main()
