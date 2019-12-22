import unittest
import day_21

class _TestDay21(unittest.TestCase):
    

    @unittest.skip("Skip")
    def _test_skip(self):
        self.assertEqual(day_21.getAnwer(1),0)


        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_21_test.py

