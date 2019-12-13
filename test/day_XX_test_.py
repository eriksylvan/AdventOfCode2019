import unittest
import day_12

class TestDay12(unittest.TestCase):
    

   # @unittest.skip("Skip")
    def test_skip(self):
        self.assertEqual(day_12.getAnwer(1),0)


        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_12_test.py

