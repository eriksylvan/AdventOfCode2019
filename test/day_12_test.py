import unittest
import day_12


class TestDay12(unittest.TestCase):
    def test_example1_0_step(self):
        eTot, outData = day_12.getPlanestData(example1, 0)
        self.assertEqual(outData,
                         ['pos=<x=-1,y=0,z=2>,vel=<x=0,y=0,z=0>',
                          'pos=<x=2,y=-10,z=-7>,vel=<x=0,y=0,z=0>',
                          'pos=<x=4,y=-8,z=8>,vel=<x=0,y=0,z=0>',
                          'pos=<x=3,y=5,z=-1>,vel=<x=0,y=0,z=0>'])

    def test_example1_1_step(self):
        eTot, outData = day_12.getPlanestData(example1, 1)
        self.assertEqual(outData,
                            ['pos=<x=2,y=-1,z=1>,vel=<x=3,y=-1,z=-1>',
                            'pos=<x=3,y=-7,z=-4>,vel=<x=1,y=3,z=3>',
                            'pos=<x=1,y=-7,z=5>,vel=<x=-3,y=1,z=-3>',
                            'pos=<x=2,y=2,z=0>,vel=<x=-1,y=-3,z=1>'])

    def test_example1_2_step(self):
        eTot, outData = day_12.getPlanestData(example1, 2)
        self.assertEqual(outData,
                            ['pos=<x=5,y=-3,z=-1>,vel=<x=3,y=-2,z=-2>',
                            'pos=<x=1,y=-2,z=2>,vel=<x=-2,y=5,z=6>',
                            'pos=<x=1,y=-4,z=-1>,vel=<x=0,y=3,z=-6>',
                            'pos=<x=1,y=-4,z=2>,vel=<x=-1,y=-6,z=2>'])
    
    def test_example1_5_step(self):
        eTot, outData = day_12.getPlanestData(example1, 5)
        self.assertEqual(outData,
                            ['pos=<x=-1,y=-9,z=2>,vel=<x=-3,y=-1,z=2>',
                            'pos=<x=4,y=1,z=5>,vel=<x=2,y=0,z=-2>',
                            'pos=<x=2,y=2,z=-4>,vel=<x=0,y=-1,z=2>',
                            'pos=<x=3,y=-7,z=-1>,vel=<x=1,y=2,z=-2>'])

    def test_example1_10_step(self):
        eTot, outData = day_12.getPlanestData(example2, 10)
        self.assertEqual(outData,
                            ['pos=<x=2,y=1,z=-3>,vel=<x=-3,y=-2,z=1>',
                            'pos=<x=1,y=-8,z=0>,vel=<x=-1,y=1,z=3>',
                            'pos=<x=3,y=-6,z=1>,vel=<x=3,y=2,z=-3>',
                            'pos=<x=2,y=0,z=4>,vel=<x=1,y=-1,z=-1>'])
    
    def test_example2_10_step(self):
        eTot, outData = day_12.getPlanestData(example2, 10)
        self.assertEqual(outData,
                            ['pos=<x=-9,y=-10,z=1>,vel=<x=-2,y=-2,z=-1>',
                            'pos=<x=4,y=10,z=9>,vel=<x=-3,y=7,z=-2>',
                            'pos=<x=8,y=-10,z=-3>,vel=<x=5,y=-1,z=-2>',
                            'pos=<x=5,y=-10,z=3>,vel=<x=0,y=-4,z=5>'])
        self.assertEqual(eTot, 179)


    def test_example2_100_step(self):
        eTot, outData = day_12.getPlanestData(example2, 100)
        self.assertEqual(outData,
                            ['pos=<x=8,y=-12,z=-9>,vel=<x=-7,y=3,z=0>',
                            'pos=<x=13,y=16,z=-3>,vel=<x=3,y=-11,z=-5>',
                            'pos=<x=-29,y=-11,z=-1>,vel=<x=-3,y=7,z=4>',
                            'pos=<x=16,y=-13,z=23>,vel=<x=7,y=1,z=1>'])
        self.assertEqual(eTot, 1940)



###############################
# Testinput
###############################
example1 = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
example2 = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]
