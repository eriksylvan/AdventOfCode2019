import unittest
import day_07
from intcode_computer import IntcodeComputer

class TestIntCodeComputer(unittest.TestCase):
    
    def runIntCode(self,code,input = []):
        IntCode = IntcodeComputer(code)
        output = IntCode.run_program(input)
        return output

    # @unittest.skip("Skipping")
    # Example 1, input equal 8, Input == 8 -> 1
    def test_equal_to_8_position(self):
        self.assertEqual(self.runIntCode([3,9,8,9,10,9,4,9,99,-1,8],input=[8]), [1])
        self.assertEqual(self.runIntCode([3,9,8,9,10,9,4,9,99,-1,8],input=[9]), [0])

    # @unittest.skip("Skipping")
    # Example 2, input less than 8, Input == 8 --> 0
    def test_less_than_8_position(self):
        self.assertEqual(self.runIntCode([3,9,7,9,10,9,4,9,99,-1,8], input=[8]), [0])
        self.assertEqual(self.runIntCode([3,9,7,9,10,9,4,9,99,-1,8], input=[7]), [1])

    # @unittest.skip("Skipping")
    # Example 3, input equal 8, Input == 8 --> 0 
    def test_equal_to_8_immediate(self):
        self.assertEqual(self.runIntCode([3,3,1108,-1,8,3,4,3,99], input=[8]), [1])
        self.assertEqual(self.runIntCode([3,3,1108,-1,8,3,4,3,99], input=[0]), [0])
    
    # @unittest.skip("Skipping")
    # # Example 4, input less than 8, Input == 8 --> 0 
    def test_less_than_8_immediate(self):
        self.assertEqual(self.runIntCode([3,3,1107,-1,8,3,4,3,99], input=[8]), [0])
        self.assertEqual(self.runIntCode([3,3,1107,-1,8,3,4,3,99], input=[1]), [1])
    
    # @unittest.skip("Skipping")
    # # Example 5, (using position mode), Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
    def test_jump_zero_position(self):
        self.assertEqual(self.runIntCode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], input=[0]), [0])
        self.assertEqual(self.runIntCode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], input=[5]), [1])
    
    # @unittest.skip("Skipping")
    # # Example 6, (using immediate  mode), Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
    def test_jump_zero_immediate(self):
        self.assertEqual(self.runIntCode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], input=[0]), [0])
        self.assertEqual(self.runIntCode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], input=[9]), [1])
    
    # @unittest.skip("Skipping")
    # Example 7, Lager program, input > 8 --> output 999, input == 8 --> output 1000, input > 8 --> output 1001
    def test_comparation_8(self):
        self.assertEqual(self.runIntCode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], input=[0]), [999])
        self.assertEqual(self.runIntCode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], input=[4]), [999])
        self.assertEqual(self.runIntCode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], input=[8]), [1000])
        self.assertEqual(self.runIntCode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], input=[90]), [1001])
    
    # @unittest.skip("Skipping")
    # Example 8, Lager program, input > 8 --> output 999, input == 8 --> output 1000, input > 8 --> output 1001
    def test_comparation_memory_bound_relative(self):
        self.assertEqual(self.runIntCode([209,9,22201,-40,-39,951,4,1001,99,50,13,19]),[32])
        self.assertEqual(self.runIntCode([209,9,22202,-100,-99,100,204,100,99,110,3,99]),[297])

    # Test immidiate exit
    def test_exit(self):
        self.assertEqual(self.runIntCode([99,1,2,3,4,5,6,7]),[])
    
            # 1   addOP
            # 2   multiplyOP
            # 3   inputOP
            # 4   outputOP
            # 5   jumpTrueOP
            # 6   jumpFalseOP
            # 7   lessOP
            # 8   equalOP
        
   