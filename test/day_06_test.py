import unittest
import day_06

class TestDay06(unittest.TestCase):
    



    def test_number_of_orbits(self):
        self.assertEqual(day_06.noOfOrbits(['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L])']), 42)
      


        
if __name__ == '__main__':
    unittest.main()



# Run tests from terminal:
# $ python -m unittest day_06_test.py

