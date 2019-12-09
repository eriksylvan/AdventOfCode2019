import unittest
import day_07

class TestDay07(unittest.TestCase):
    
    def test_max_thruster_signal(self):
        self.assertEqual(day_07.maxThrusterSignal([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]),54321)
        self.assertEqual(day_07.maxThrusterSignal([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]),43210)
        self.assertEqual(day_07.maxThrusterSignal([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]),65210)

# IntCode = IntcodeComputer([1105, 1, 4, 4, 99])
    # # IntCode.perform_one_operation(0)
    # IntCode.run_program()
    # print(IntCode._intCodeProgram)

    # # Example 1, input equal 8, Input == 8 -> 1
    # print("Example 1, input equal 8, Input == 8 -> 1")
    # IC = IntcodeComputer([3,9,8,9,10,9,4,9,99,-1,8])
    # IC.run_program()
    # print(IC._intCodeProgram)

    # # Example 2, input less than 8, Input == 8 --> 0 
    # print("Example 2, input less than 8, Input == 8 --> 0")
    # IC = IntcodeComputer([3,9,7,9,10,9,4,9,99,-1,8])
    # IC.run_program()
    # print(IC._intCodeProgram)

    # # Example 3, input equal 8, Input == 8 --> 0 
    # print("Example 3, input equal 8, Input == 8 --> 0")
    # IC = IntcodeComputer([3,3,1108,-1,8,3,4,3,99])
    # IC.run_program()
    # print(IC._intCodeProgram)

    # # Example 4, input less than 8, Input == 8 --> 0 
    # print("Example 4, input less than 8, Input == 8 --> 0")
    # IC = IntcodeComputer([3,3,1107,-1,8,3,4,3,99])
    # IC.run_program()
    # print(IC._intCodeProgram)


    # # Example 5, (using position mode), Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
    # print('Example 5, (using position mode), Jump test Input == 0 --> 0, Input != 0 --> 1 )')
    # IC = IntcodeComputer([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
    # IC.run_program()
    # print(IC._intCodeProgram)


    # # Example 6, (using immediate  mode), Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
    # print('Example 6, (using position mode), Jump test Input == 0 --> 0, Input != 0 --> 1 )')
     
    # IC = IntcodeComputer([3,3,1105,-1,9,1101,0,0,12,4,12,99,1]) 
    # IC.run_program()
    # print(IC._intCodeProgram)

    # # # Example 7, Lager program, input > 8 --> output 999, input == 8 --> output 1000, input > 8 --> output 1001
    # print('Example 7, Lager program, input > 8 --> output 999, input == 8 --> output 1000, input > 8 --> output 1001')
    # IC = IntcodeComputer([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
    # IC.run_program()
    # print(IC._intCodeProgram)


            # 1   addOP8
            # 2   multiplyOP
            # 3   inputOP
            # 4   outputOP
            # 5   jumpTrueOP
            # 6   jumpFalseOP
            # 7   lessOP
            # 8   equalOP
        

    def test_max_thruster_feedbackLoop(self):
        self.assertEqual(day_07.maxThrusterSignalFeedbackLoop([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]),139629729) # (from phase setting sequence 9,8,7,6,5)
        self.assertEqual(day_07.maxThrusterSignalFeedbackLoop([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]),18216) # (from phase setting sequence 9,7,8,5,6)




if __name__ == '__main__':
    unittest.main()

# Run tests from terminal:
# $ python -m unittest day_07_test.py