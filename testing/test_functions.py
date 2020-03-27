import unittest
import calc


class TestCalc(unittest.TestCase):
    # do not rename it with xxx_test it wll be skipped 
    def test_add(self):
        self.assertEqual(calc.add(2,1),3)
        self.assertEqual(calc.add(2,-1),1)
        self.assertEqual(calc.add(-2,1),-1)
    
    def test_minus(self):
        self.assertEqual(calc.substract(2,1),1)
        self.assertEqual(calc.substract(2,-1),3)
        self.assertEqual(calc.substract(-2,1),-3)
   
    def test_multiply(self):
        self.assertEqual(calc.multiply(2,1),2)
        self.assertEqual(calc.multiply(2,-1),-2)
        self.assertEqual(calc.multiply(-2,1),-2)

    def test_devide(self):
        self.assertEqual(calc.devide(2,1),2)
        self.assertEqual(calc.devide(2,-1),-2)
        self.assertEqual(calc.devide(-2,-1),2)
        self.assertRaises(ValueError,calc.devide,10,0)
        # we can do the same ith context manager 
        # to test exception use this
        with self.assertRaises(ValueError):
            calc.devide(10,0)


 




if __name__ == "__main__":
    unittest.main()

        