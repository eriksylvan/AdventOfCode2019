import unittest
import day_05

class TestDay05day_05(unittest.TestCase):
    
    def test_diagnostic_program(self):
        self.assertEqual(day_05.runDiagnosticProgram([1002,4,3,4,33]), 0)


        
            

        
if __name__ == '__main__':
    unittest.main()



# Run tests from terminal:
# $ python -m unittest day_05_test.py

