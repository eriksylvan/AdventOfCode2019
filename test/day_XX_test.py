import unittest
import day_XX

class _TestDayXX(unittest.TestCase):
    

    @unittest.skip("Skip")
    def _test_skip(self):
        self.assertEqual(day_XX.getAnwer(1),0)


        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_XX_test.py

