import unittest
import day_19

class TestDa19(unittest.TestCase):
    

   # @unittest.skip("Skip")
    def test_skip(self):
        self.assertEqual(day_19.getAnwer(0),0)

        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day19_test.py

