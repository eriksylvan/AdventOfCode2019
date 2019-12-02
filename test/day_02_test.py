import unittest
import day_02

class TestDay02(unittest.TestCase):
    
    def test_intcode(self):
        self.assertEqual(day_02.intcode([1,0,0,0,99]),[2,0,0,0,99])
        self.assertEqual(day_02.intcode([2,3,0,3,99]),[2,3,0,6,99])
        self.assertEqual(day_02.intcode([2,4,4,5,99,0]),[2,4,4,5,99,9801])
        self.assertEqual(day_02.intcode([1,1,1,4,99,5,6,0,99]),[30,1,1,4,2,5,6,0,99])

if __name__ == '__main__':
    unittest.main()



# Run tests from terminal:
# $ python -m unittest day_02_test.py

