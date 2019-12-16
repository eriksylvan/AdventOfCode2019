import unittest
import day_16

class TestDay16(unittest.TestCase):
    

# @unittest.skip("Skip")
    def test_FFT_example1_fisrtphase(self):
        self.assertEqual(day_16.getFFT('12345678',1),'48226158')
    
    def test_FFT_example1_nextphase(self):
        self.assertEqual(day_16.getFFT('48226158',1),'34040438')
    
    def test_FFT_example1_phase3(self):
        self.assertEqual(day_16.getFFT('12345678',3),'03415518')

    def test_FFT_example1_phase4(self):
        self.assertEqual(day_16.getFFT('12345678',4),'01029498')


    def test_FFT_example2(self):
        self.assertEqual(day_16.getFFT('80871224585914546619083218645595', 100)[0:8], '24176176') # compare first 8 digits in answer

    def test_FFT_example3(self):
        self.assertEqual(day_16.getFFT('19617804207202209144916044189917', 100)[0:8], '73745418')
        
    def test_FFT_example4(self):
        self.assertEqual(day_16.getFFT('69317163492948606335995924319873', 100)[0:8], '52432133') 
        
if __name__ == '__main__':
    unittest.main()


# Run tests from terminal:
# $ python -m unittest day_16_test.py

