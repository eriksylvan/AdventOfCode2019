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

    def test_password_2(self):
        self.assertTrue(day_04.isValidPassword2('112233'))
        self.assertFalse(day_04.isValidPassword2('123444'))
        self.assertTrue(day_04.isValidPassword2('111122'))
        
        
            

        
if __name__ == '__main__':
    unittest.main()



# Run tests from terminal:
# $ python -m unittest day_04_test.py

