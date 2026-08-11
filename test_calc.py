import unittest
import B18_calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        #results = B18_calc.add(21,7)
        self.assertEqual(B18_calc.add(21,7), 28)
        self.assertEqual(B18_calc.add(20, 5), 21)
        self.assertEqual(B18_calc.add(20, 21), 30)
    def test_subtract(self):
            #results = B18_calc.add(21,7)
            self.assertEqual(B18_calc.subtract(21,7), 14)
            self.assertEqual(B18_calc.subtract(20, 5), 15)
            self.assertEqual(B18_calc.subtract(20, 21), 0)
    def test_multiply(self):
            #results = B18_calc.add(21,7)
            self.assertEqual(B18_calc.multiply(21,7), 147)
            self.assertEqual(B18_calc.multiply(20, 5), 100)
            self.assertEqual(B18_calc.multiply(20, 21), 420)
    def test_divide(self):
            #results = B18_calc.add(21,7)
            self.assertEqual(B18_calc.divide(21,7), 3)
            self.assertEqual(B18_calc.divide(20, 5), 4)
            self.assertEqual(B18_calc.divide(20, 21), 1)   

            self.assertRaises(ValueError, B18_calc.divide, 10, 0)   
            #kiểm tra xem dòng code có ném ra đúng lỗi ValueError khi chia cho 0 hay không
            #còn 1 cách khác để kiểm tra lỗi là dùng trình quản lí ngữ cảnh
            with self.assertRaises(ValueError):
                  B18_calc.divide(10,0) 
    def test_power(self):     
            self.assertEqual(B18_calc.power(2,3), 8)
            self.assertEqual(B18_calc.power(7,2), 49)                     

if __name__ == '__main__':
    unittest.main()
