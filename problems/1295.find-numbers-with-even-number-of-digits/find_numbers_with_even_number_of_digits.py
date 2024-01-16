"""Find Numbers with Even Number of Digits"""
from ast import List


class FindNumbers:
    """
    Class to find the count of numbers in the given list that have an even number of digits.
    """
    def find_numbers(self, nums: List[int]) -> int:
        """
        Finds the count of numbers in the given list that have an even number of digits.
        
        Args:
            nums (List[int]): A list of integers.
            
        Returns:
            int: The count of numbers with an even number of digits.
        """
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
