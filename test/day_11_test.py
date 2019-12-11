import unittest
import day_11

class TestDay11(unittest.TestCase):
    

   # @unittest.skip("Skip")
    def test_painting_robot(self):
        self.assertEqual(day_11.getAnwer(1),0)


        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_11_test.py

