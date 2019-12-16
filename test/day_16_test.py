import unittest
import day_16

class TestDay16(unittest.TestCase):
    

   # @unittest.skip("Skip")
    def test_skip(self):
        self.assertEqual(day_16.getFFT('12345',1),'48226158')


        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_16_test.py

