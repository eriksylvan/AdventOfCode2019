import unittest
import day_09

class TestDay09(unittest.TestCase):
    
    def test_LargeAddition(self):
        self.assertEqual(day_09.BOOSTkeycode([1102,34915192,34915192,7,4,7,99,0]), [1219070632396864])

    def test_LargeOutput(self):
        self.assertEqual(day_09.BOOSTkeycode([104,1125899906842624,99]),[1125899906842624])


    # @unittest.skip("demonstrating skipping")
    def test_QuineComputing(self):
        self.assertEqual(day_09.BOOSTkeycode([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]),[109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
if __name__ == '__main__':
    unittest.main()

# Run tests from terminal:
# $ python -m unittest day_09_test.py