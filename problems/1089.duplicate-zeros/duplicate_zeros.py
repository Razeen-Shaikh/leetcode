"""
This module provides a solution for duplicating each occurrence of zero in the input array 'arr'.
"""
from ast import List


class Solution:
    """
    This class provides a solution for duplicating each occurrence of zero in the input array 'arr'.
    """
    def duplicate_zeros(self, arr: List[int]) -> None:
        """
        Duplicate each occurrence of zero in the input array 'arr'.
        
        Args:
            arr (List[int]): The input array
            
        Returns:
            None
        """
        temp = []
        for num in arr:
            if num == 0:
                temp.append(0)
                temp.append(0)
            else: temp.append(num)
        
        for i, value in enumerate(arr):
            arr[i] = temp[i]
