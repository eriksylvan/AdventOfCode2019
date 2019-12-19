import unittest
import day_17

class TestDay17(unittest.TestCase):
    
    def test_findIntersections(self):
        expSet = set([(4, 2), (2, 2), (4, 6), (4, 10)])
        self.assertEqual(set(day_17.findIntersections(map1)),expSet)

    def test_calcAlignmentParameters(self):
        self.assertEqual(day_17.calcAlignmentParameters(map1), 76)

    def test_findRobot(self):
        self.assertEqual(day_17.findRobot(map1), ((10,6), '^'))

    def test_followPathMap1(self):
        self.assertEqual(day_17.followPath(map1),'4R2R2R12R2R6R4R4R6')

    def test_followPathMap2(self):
        self.assertEqual(day_17.followPath(map2),'R2R2L10R2R4L2R3R6R5R6')
    
    def test_followPathMap3(self):
        self.assertEqual(day_17.followPath(map3),'R8R8R4R4R8L6L2R4R4R8R8R8L6L2')        
        
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
'..#####...^..'] # 4R2R2R12R2R6R4R4R6

map2 = [
'..#.####.....',
'..#.#..#.....',
'#####..#.....',
'#.#....#.....',
'###########..',
'..#....#..#..',
'..######..##v'] #R2R2L10R2R4L2R3R6R5R6

map3 = [
'#######...#####',
'#.....#...#...#',
'#.....#...#...#',
'......#...#...#',
'......#...###.#',
'......#.....#.#',
'^########...#.#',
'......#.#...#.#',
'......#########',
'........#...#..',
'....#########..',
'....#...#......',
'....#...#......',
'....#...#......',
'....#####......'] # R8R8R4R4R8L6L2R4R4R8R8R8L6L2