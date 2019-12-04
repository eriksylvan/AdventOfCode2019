import unittest
import day_04

class TestDay04(unittest.TestCase):
    
    def test_password(self):
        self.assertFalse(day_04.isValidPassword('11111'))
        self.assertTrue(day_04.isValidPassword('111111'))
        self.assertFalse(day_04.isValidPassword('1111111'))
        self.assertFalse(day_04.isValidPassword('223450'))
        self.assertFalse(day_04.isValidPassword('123789'))
        self.assertTrue(day_04.isValidPassword('235589'))

        
if __name__ == '__main__':
    unittest.main()



# Run tests from terminal:
# $ python -m unittest day_04_test.py

