import unittest
import day_17

class TestDay17(unittest.TestCase):
    
    def test_findIntersections(self):
        expSet = set([(4, 2), (2, 2), (4, 6), (4, 10)])
        self.assertEqual(set(day_17.findIntersections(map1)),expSet)

    def test_calcAlignmentParameters(self):
        self.assertEqual(day_17.calcAlignmentParameters(map1), 76)



        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_17_test.py

##########################
#   TEST DATA
##########################

map1 = [
'..#..........',
'..#..........',
'#######...###',
'#.#...#...#.#',
'#############',
'..#...#...#..',
'..#####...^..']