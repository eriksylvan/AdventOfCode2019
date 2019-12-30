import unittest
import day_18

class TestDay18(unittest.TestCase):
    

    #@unittest.skip("Skip")
    def test_skip(self):
        self.assertEqual(day_18.getAnwer(3),0)


        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_18_test.py

