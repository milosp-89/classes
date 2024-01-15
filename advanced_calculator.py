""" Python Calculator Class """

# import necesary library/module:
import math as mth

class Calculator():
    
    """
    Base Class to activate different math methods within objects\n
    * Methods:\n
    1. add: summary of one or more numbers\n
    2. sub: substraction of one or more numbers between each other\n
    3. mult: multiplication of one or more numbers between each other\n
    4. div: division between one or more numbers between each other
    """
    
    def __init__(self):
        pass
    
    """
    Constructor: doesent have any attributes/parameters
    """
    
    def add(self, nums):
        
        """
        This method will conduct a sum operation on all numbers detected within a list\n
        NOTE1: if list is empty result will be 0\n
        NOTE2: if float numbers detected, result will be rounded up to maximum .xx two decimals\n
        :param1 nums: this is the parameter representing a list of numbers\n
        :return: it will return ==> a summary of all numbers as either a whole number or float with maximum two decimals
        """
        
        try: return round(sum([num for num in nums]), 2)
        except Exception: return 0
    
    def sub(self, nums):
        
        """
        This method will conduct a substraction operation on all numbers detected within a list\n
        NOTE1: if list is empty result will be 0\n
        NOTE2: if float numbers detected, result will be rounded up to maximum .xx two decimals\n
        :param1 nums: this is the parameter representing a list of numbers\n
        :return: it will return ==> a summary of all substracted numbers (between each other) either as a whole number or float with maximum two decimals
        """
        
        from functools import reduce as r
        try: return round(r(lambda x, y: x - y, nums), 2)
        except TypeError: return 0
    
    def mult(self, nums):
        
        """
        This method will conduct a multiplication operation on all numbers detected within a list\n
        NOTE1: if list is empty result will be 0\n
        NOTE2: if there is a zero 0, result will be a 0\n
        NOTE3: if float numbers detected, result will be rounded up to maximum .xx two decimals\n
        :param1 nums: this is the parameter representing a list of numbers\n
        :return: it will return ==> a summary of all multiplied numbers (between each other) either as a whole number or float with maximum two decimals
        """
        
        if len(nums) == 0:
            return 0
        else:
            result = 1
            for n in nums:
                try:
                    result = result * n
                except Exception:
                    return 0
            return round(result, 2)
  
    def div(self, nums):
        
        """
        This method will conduct a division operation on all numbers detected within a list\n
        NOTE1: if list is empty result will be 0\n
        NOTE2: if there is a zero 0, result will be a 0\n
        NOTE3: if float numbers detected, result will be rounded up to maximum .xx two decimals\n
        :param1 nums: this is the parameter representing a list of numbers\n
        :return: it will return ==> a summary of all divided numbers (between each other) either as a whole number or float with maximum two decimals
        """
        
        if len(nums) == 0:
            return 0
        else:
            result = nums[0]
            for n in range(1, len(nums)):
                try: result = result / nums[n]
                except Exception: return 0
            return round(result, 2)
    
class AdvancedCalculator(Calculator):
    
    """
    Child Class to activate different math methods within objects\n
    * Methods:\n
    1. power: power of two numbers\n
    2. floor: flooring all numbers one by one\n
    """
    
    def __init__(self):
        pass
    
    """
    Constructor: doesent have any attributes/parameters
    """
    
    def power(self, num1, num2):
        
        """
        This method will conduct a power operation on two numbers\n
        NOTE1: if list is empty result will be 0\n
        NOTE2: if only one number provided, result will be a zero\n
        NOTE3: if float numbers detected, result will be rounded up to maximum .xx two decimals\n
        :param1 num1: this is the parameter representing first number\n
        param2 num2: this is the parameter representing second number\n
        :return: it will return ==> a power of two numbers (num1 and num2) either as a whole number or float with maximum two decimals
        """
        
        try:
            if num1 == None or num2 == None:
                return 0
            else:
                return round(mth.pow(num1, num2), 2)
        except Exception:
            return 0
         
    def floor(self, nums):
        
        """
        This method will conduct a flooring operation on all numbers detected within a list\n
        NOTE1: if list is empty result will be 0\n
        NOTE2: if float numbers detected, result will be rounded up to maximum .xx two decimals\n
        :param1 nums: this is the parameter representing a list of numbers\n
        :return: it will return ==> a list of floored numbers as int
        """
        
        if len(nums) == 0:
            return 0
        else:
            try:
                return list(map(lambda x: int(mth.floor(x)), nums))
            except Exception:
                return 0