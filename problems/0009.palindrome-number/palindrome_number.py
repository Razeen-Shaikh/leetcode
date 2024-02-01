"""Check for palindrome"""

class Solution:
    """
    This class provides methods for checking whether an integer is a palindrome.
    """
    def is_palindrome(self, x: int) -> bool:
        """
        Check if the given integer is a palindrome.

        Args:
            x (int): The integer to be checked for palindrome.

        Returns:
            bool: True if the integer is a palindrome, False otherwise.
        """
        x_list = [i for i in str(x)]
        return x_list == x_list[::-1]
