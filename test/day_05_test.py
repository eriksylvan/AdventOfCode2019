import unittest
import day_05
from intcode_computer import IntcodeComputer 

class TestDay05(unittest.TestCase):
    



    def test_multiply(self):
        IC = IntcodeComputer([1002,4,3,4,33])
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1002,4,3,4,12])


    def test_add(self):
        IC = IntcodeComputer([1002,2,2,4,33])
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1002,2,2,4,4])

    def test_input(self):
        IC = IntcodeComputer([1003,4,2,4,33])
        IC.perform_one_operation(0)
        self.assertEqual(IC._intCodeProgram,[1002,2,2,4,4])

# @unittest.SkipTest('Not implemeted yet')
#     def test_diagnostic_program(self):
#         self.assertEqual(day_05.runDiagnosticProgram([1002,4,3,4,33]), 0)


        
            

        
if __name__ == '__main__':
    unittest.main()



# Run tests from terminal:
# $ python -m unittest day_05_test.py

