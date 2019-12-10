import unittest
import day_10

class TestDay10(unittest.TestCase):
    
    def test_AstroidMap1(self):
        self.assertEqual(day_10.findBestMonitoringStation(AstridMap1),(8,(3,4)))

    def test_AstroidMap2(self):
        self.assertEqual(day_10.findBestMonitoringStation(AstridMap2),(33,(5,8)))

    def test_AstroidMap3(self):
        self.assertEqual(day_10.findBestMonitoringStation(AstridMap3),(35,(1,2)))

    def test_AstroidMap4(self):
        self.assertEqual(day_10.findBestMonitoringStation(AstridMap4),(41,(6,3)))

    def test_AstroidMap5(self):
        self.assertEqual(day_10.findBestMonitoringStation(AstridMap5),(210,(11,13)))


    @unittest.skip("Skip")
    def test_test_AstroidMap100(self):
        self.assertEqual(day_10.contVisibleAsroids(AstridMap100),(100,(99,99)))
        
        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_10_test.py



##########################################
#   TEST DATA
##########################################

AstridMap1 = [
'.#..#',
'.....',
'#####',
'....#',
'...##'
]

AstridMap2 = [
'......#.#.',
'#..#.#....',
'..#######.',
'.#.#.###..',
'.#..#.....',
'..#....#.#',
'#..#....#.',
'.##.#..###',
'##...#..#.',
'.#....####'
]

AstridMap3 = [
'#.#...#.#.',
'.###....#.',
'.#....#...',
'##.#.#.#.#',
'....#.#.#.',
'.##..###.#',
'..#...##..',
'..##....##',
'......#...',
'.####.###.'
]

AstridMap4 = [
'.#..#..###',
'####.###.#',
'....###.#.',
'..###.##.#',
'##.##.#.#.',
'....###..#',
'..#.#..#.#',
'#..#.#.###',
'.##...##.#',
'.....#.#..'
]

AstridMap5 = [
'.#..##.###...#######',
'##.############..##.',
'.#.######.########.#',
'.###.#######.####.#.',
'#####.##.#.##.###.##',
'..#####..#.#########',
'####################',
'#.####....###.#.#.##',
'##.#################',
'#####.##.###..####..',
'..######..##.#######',
'####.##.####...##..#',
'.#####..#.######.###',
'##...#.##########...',
'#.##########.#######',
'.####.#.###.###.#.##',
'....##.##.###..#####',
'.#.#.###########.###',
'#.#.#.#####.####.###',
'###.##.####.##.#..##'
]

AstridMap100 = ['']