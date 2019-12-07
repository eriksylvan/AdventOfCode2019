import unittest
import day_05
from intcode_computer import IntcodeComputer 

class TestDay05(unittest.TestCase):
    



    def test_multiply(self):
        IC = IntcodeComputer([1002,4,3,4,33])
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1002,4,3,4,99])


    def test_add(self):
        IC = IntcodeComputer([1001,2,2,4,33])
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1001,2,2,4,4])

    def test_jumpTrue(self):
        IC = IntcodeComputer([1105, 1, 4, 4, 99])
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1105, 1, 4, 4, 99])
        self.assertEqual(IC._memoryPosition,4)

    def test_jumpFalse(self):
        IC = IntcodeComputer([1106, 0, 4, 4, 99])
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1106, 0, 4, 4, 99])
        self.assertEqual(IC._memoryPosition,4)

    
    def test_jumpFalse2(self):
        IC = IntcodeComputer([1006, 4, 5, 99, 5, 6 ]) # Do not jump
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1006, 4, 5, 99, 5, 6])
        self.assertEqual(IC._memoryPosition,3)

    def test_jumpFalse3(self):
        IC = IntcodeComputer([1006, 4, 5, 99, 0, 6 ]) # do jump to pos 5
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1006, 4, 5, 99, 0, 6])
        self.assertEqual(IC._memoryPosition,5)

    def test_less(self):
        IC = IntcodeComputer([1107, 1, 2, 3, 99]) # less than
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1107, 1, 2, 1, 99])
        self.assertEqual(IC._memoryPosition,4)
    
    def test_less2(self):
        IC = IntcodeComputer([1107, 2, 1, 3, 99]) # greater than
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1107, 2, 1, 0, 99])
        self.assertEqual(IC._memoryPosition,4)
    
    def test_great(self):
        IC = IntcodeComputer([1108, 1, 2, 3, 99]) # less than
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1108, 1, 2, 0, 99])
        self.assertEqual(IC._memoryPosition,4)

    def test_great2(self):
        IC = IntcodeComputer([1108, 2, 1, 3, 99]) # greater than
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1108, 2, 1, 1, 99])
        self.assertEqual(IC._memoryPosition,4)

    def test_equal(self):
        IC = IntcodeComputer([1109, 1, 1, 3, 99]) # equal
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1109, 1, 1, 1, 99])
        self.assertEqual(IC._memoryPosition,4)

    def test_equal2(self):
        IC = IntcodeComputer([1109, 2, 1, 3, 99]) # not equal
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1109, 2, 1, 0, 99])
        self.assertEqual(IC._memoryPosition,4)

    def test_example1(self):
        IC = IntcodeComputer([3,9,8,9,10,9,4,9,99,-1,8])
        IC.run_program()
        # self.assertEqual(IC._intCodeProgram,[])
        # self.assertEqual(IC._memoryPosition,4)

    def test_example2(self):
        IC = IntcodeComputer([103,9,8,9,10,9,4,9,99,-1,8])
        IC.run_program()
        # self.assertEqual(IC._intCodeProgram,[])
        # self.assertEqual(IC._memoryPosition,4)

if __name__ == '__main__':
    unittest.main()



# Run tests from terminal:
# $ python -m unittest day_05_test.py

