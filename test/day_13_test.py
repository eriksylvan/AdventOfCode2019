import unittest
import day_13

class TestDay13(unittest.TestCase):
    

   # @unittest.skip("Skip")
    def test_skip(self):
        self.assertEqual(day_13.getAnwer(1),0)


        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_13_test.py

