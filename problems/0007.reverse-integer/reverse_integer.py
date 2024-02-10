"""
Module for reversing integers.
"""

class Solution:
    """
    This class provides methods for reversing integers.
    """
    def reverse(self, x: int) -> int:
        """
        Reverses the given integer.

        Args:
            x (int): The input integer to be reversed.

        Returns:
            int: The reversed integer.

        Raises:
            None
        """
        if x < 0:
            reversed_str = str(x)[1:][::-1]
            reversed_int = int(reversed_str)
            reversed_int *= -1
        else:
            reversed_str = str(x)[::-1]
            reversed_int = int(reversed_str)

        # Check if the reversed integer falls within the 32-bit signed integer range
        if -(2**31) <= reversed_int <= (2**31 - 1):
            return reversed_int
        else:
            return 0
