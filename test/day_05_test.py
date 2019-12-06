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

        
            

        
if __name__ == '__main__':
    unittest.main()



# Run tests from terminal:
# $ python -m unittest day_05_test.py

