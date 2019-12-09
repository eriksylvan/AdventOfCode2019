import unittest
import day_08

class TestDay08(unittest.TestCase):
    
    def test_layerFewest0(self):
        self.assertEqual(day_08.getAnswerPartOne('123456789012',3,2),1)
        self.assertEqual(day_08.getAnswerPartOne('101010102002100200201102111121101010102222100200201102111121',6,5),96)


if __name__ == '__main__':
    unittest.main()

# Run tests from terminal:
# $ python -m unittest day_08_test.py