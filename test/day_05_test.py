import unittest
import day_05
import time
from intcode_computer import IntcodeComputer 

class TestDay05(unittest.TestCase):
    



    def test_multiply(self):
        IC = IntcodeComputer([1002,4,3,4,1])
        IC.perform_one_operation(0)
        self.assertEqual(list(IC._intCodeProgramDict.values()),[1002,4,3,4,3])


    def test_add(self):
        IC = IntcodeComputer([1001,2,2,4,-1])
        IC.perform_one_operation(0)
        self.assertEqual(list(IC._intCodeProgramDict.values()),[1001,2,2,4,4])

    def test_jumpTrue(self):
        IC = IntcodeComputer([1105, 1, 4, 4, 99])
        IC.perform_one_operation(0)
        self.assertEqual(list(IC._intCodeProgramDict.values()),[1105, 1, 4, 4, 99])
        self.assertEqual(IC._memoryPosition,4)

    def test_jumpFalse(self):
        IC = IntcodeComputer([1106, 0, 4, 4, 99])
        IC.perform_one_operation(0)
        self.assertEqual(list(IC._intCodeProgramDict.values()),[1106, 0, 4, 4, 99])
        self.assertEqual(IC._memoryPosition,4)

    
    def test_jumpFalse2(self):
        IC = IntcodeComputer([1006, 4, 5, 99, 5, 6 ]) # Do not jump
        IC.perform_one_operation(0)
        self.assertEqual(list(IC._intCodeProgramDict.values()),[1006, 4, 5, 99, 5, 6])
        self.assertEqual(IC._memoryPosition,3)

    def test_jumpFalse3(self):
        IC = IntcodeComputer([1006, 4, 5, 99, 0, 6 ]) # do jump to pos 5
        IC.perform_one_operation(0)
        self.assertEqual(list(IC._intCodeProgramDict.values()),[1006, 4, 5, 99, 0, 6])
        self.assertEqual(IC._memoryPosition,5)

    def test_less(self):
        IC = IntcodeComputer([1107, 1, 2, 3, 99]) # less than
        IC.perform_one_operation(0)
        self.assertEqual(list(IC._intCodeProgramDict.values()),[1107, 1, 2, 1, 99])
        self.assertEqual(IC._memoryPosition,4)
    
    def test_less2(self):
        IC = IntcodeComputer([1107, 2, 1, 3, 99]) # greater than
        IC.perform_one_operation(0)
        self.assertEqual(list(IC._intCodeProgramDict.values()),[1107, 2, 1, 0, 99])
        self.assertEqual(IC._memoryPosition,4)
    
    def test_equal(self):
        IC = IntcodeComputer([1108, 1, 1, 3, 99]) # equal
        IC.perform_one_operation(0)
        self.assertEqual(IC.readMem(3), 1)
        self.assertEqual(IC._memoryPosition, 4)

    def test_equal2(self):
        IC = IntcodeComputer([1108, 2, 1, 3, 99]) # not equal
        IC.perform_one_operation(0)
        self.assertEqual(IC.readMem(3), 0)
        self.assertEqual(IC._memoryPosition,4)


#########################################################################################

    def test_example1(self):
        IC = IntcodeComputer([3,7,8,7,8,7,99,-1,8])
        IC.run_program([8])
        self.assertEqual(IC.readMem(7), 1)


    def test_example2(self):
        IC = IntcodeComputer([103,7,8,7,8,9,99,-1,8])
        IC.run_program([8])
        self.assertEqual(IC.readMem(7), -1)
        self.assertEqual(IC.readMem(1), 8)

if __name__ == '__main__':
    unittest.main()

            # 1   addOP8                Addition            (r1,r2,w):  r1 + r2 -> w
            # 2   multiplyOP            Multiplication      (r1,r2,w):  r1 * r2 -> w
            # 3   inputOP               Read inpot          (w):        input -> w 
            # 4   outputOP              Output              (r):        r -> output 
            # 5   jumpTrueOP            If True then jump   (r1,r2,r3): If r1==r2 Then jump to r3
            # 6   jumpFalseOP           If False then jump  (r1,r2,r3): If r1!=r2 Then jump to r3
            # 7   lessOP                Compare less than   (r1,r2,w3): If r1<=r2 Then r3 = 1
            # 8   equalOP               Compare equal       (r1,r2,w3): If r1==r2 Then r3 = 1
            # 9   adjustRelativeBaseOP  Ser Relative base   (r1):       r1 -> RelativeBase

# Run tests from terminal:
# $ python -m unittest day_05_test.py

