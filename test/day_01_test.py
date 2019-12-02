import unittest
import day_01

class TestDay01(unittest.TestCase):
    
    def test_fuel_calculation(self):
        self.assertEqual(day_01.fuel_calculator(12), 2)
        self.assertEqual(day_01.fuel_calculator(14), 2)
        self.assertEqual(day_01.fuel_calculator(1969), 654)
        self.assertEqual(day_01.fuel_calculator(100756), 33583)

    def test_fuel_calculator_inc_fuel(self):
        self.assertEqual(day_01.fuel_calculator_inc_fuel(14), 2)
        self.assertEqual(day_01.fuel_calculator_inc_fuel(1969), 966)
        self.assertEqual(day_01.fuel_calculator_inc_fuel(100756), 50346)

if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_01_test.py 