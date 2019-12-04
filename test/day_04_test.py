import unittest
import day_04

class TestDay04(unittest.TestCase):
    
    def test_password(self):
        self.assertTrue(day_04.isValidPassword('111111'))
        self.assertTrue(day_04.isValidPassword('223450'))
        self.assertTrue(day_04.isValidPassword('123789'))

        
if __name__ == '__main__':
    unittest.main()



# Run tests from terminal:
# $ python -m unittest day_04_test.py

