import unittest
import day_09

class TestDay09(unittest.TestCase):
    
    def test_max_thruster_signal(self):
        self.assertEqual(day_09.BOOSTkeycode([1102,34915192,34915192,7,4,7,99,0]), [1219070632396864])
        
if __name__ == '__main__':
    unittest.main()

# Run tests from terminal:
# $ python -m unittest day_09_test.py