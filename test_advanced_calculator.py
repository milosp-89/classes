""" unit testing of Calculator CLass """

from advanced_calculator import AdvancedCalculator
import unittest

# class:
class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        
        """ setUp class variable """
        
        self.ac = AdvancedCalculator() # instance of the Calculator class
    
    def test_add(self):
        
        """
        Test one: testing addition operation via add method on multiple approaches
        """
        
        # empty list:
        self.assertEqual(self.ac.add([]), 0, "Should be 0")
        
        # with zero - 0:
        self.assertEqual(self.ac.add([0]), 0, "Should be 0")
        
        # whole numbers - int:
        self.assertEqual(self.ac.add([1]), 1, "Should be 1")
        self.assertEqual(self.ac.add([0, -5]), -5, "Should be -5")
        self.assertEqual(self.ac.add([2, 0]), 2, "Should be 2")
        self.assertEqual(self.ac.add([1,4,8]), 13, "Should be 13")
        self.assertEqual(self.ac.add([-3, 1]), -2, "Should be -2")
        self.assertEqual(self.ac.add([-4, -4]), -8, "Should be -8")
        
        # floating point numbers - float:
        self.assertEqual(self.ac.add([2.34]), 2.34, "Should be 2.34")
        self.assertEqual(self.ac.add([2.11223]), 2.11, "Should be 2.11")
        self.assertEqual(self.ac.add([0, -5.1]), -5.1, "Should be -5.1")
        self.assertEqual(self.ac.add([4.63, 0]), 4.63, "Should be 4.63")
        self.assertEqual(self.ac.add([1.234,4.998534,8.9863]), 15.22, "Should be 15.22")
        self.assertEqual(self.ac.add([-3.54, 1]), -2.54, "Should be -2.54")
        self.assertEqual(self.ac.add([-4.23, -4.37]), -8.6, "Should be -8.6")
        
        
    def test_sub(self):
        
        """
        Test two: testing substruction operation via method on multiple approaches
        """
        
        # empty list:
        self.assertEqual(self.ac.sub([]), 0, "Should be 0")
        
        # with zero - 0:
        self.assertEqual(self.ac.sub([0]), 0, "Should be 0")
        
        # whole numbers - int:
        self.assertEqual(self.ac.sub([1]), 1, "Should be 1")
        self.assertEqual(self.ac.sub([0, -5]), 5, "Should be 5")
        self.assertEqual(self.ac.sub([2, 0]), 2, "Should be 2")
        self.assertEqual(self.ac.sub([1,4,8]), -11, "Should be -11")
        self.assertEqual(self.ac.sub([-3, 1]), -4, "Should be -4")
        self.assertEqual(self.ac.sub([-4, -4]), 0, "Should be 0")
        
        # floating point numbers - float:
        self.assertEqual(self.ac.sub([2.34]), 2.34, "Should be 2.34")
        self.assertEqual(self.ac.sub([2.11223]), 2.11, "Should be 2.11")
        self.assertEqual(self.ac.sub([0, -5.1]), 5.1, "Should be 5.1")
        self.assertEqual(self.ac.sub([4.63, 0]), 4.63, "Should be 4.63")
        self.assertEqual(self.ac.sub([1.234,4.998534,8.9863]), -12.75, "Should be -12.75")
        self.assertEqual(self.ac.sub([-3.54, 1]), -4.54, "Should be -4.54")
        self.assertEqual(self.ac.sub([-4.23, -4.37]), 0.14, "Should be 0.14")
        
        # the rest of the methods with a same approach!
        

if __name__ == '__main__':
    unittest.main()