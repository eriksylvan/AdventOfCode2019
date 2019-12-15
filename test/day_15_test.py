import unittest
import day_15

class TestDay15(unittest.TestCase):
    

    # @unittest.skip("Skip")
    def test_skip(self):
        self.assertEqual(day_15.getAnwer(1),0)


        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_15_test.py

