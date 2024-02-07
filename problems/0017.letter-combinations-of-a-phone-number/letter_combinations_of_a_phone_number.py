"""
Module to generate all possible combinations of letters represented by the input digits.
"""
from typing import List

class Solution:
    """
    Class to generate all possible combinations of letters represented by the input digits.
    """
    def letter_combinations(self, digits: str) -> List[str]:
        """
        Generate all possible combinations of letters represented by the input digits.

        Args:
        - digits: A string of digits representing a phone number.

        Returns:
        - A list of strings representing all possible letter combinations.

        Example:
        >>> solution = Solution()
        >>> solution.letter_combinations('23')
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        """
        if not digits:
            return []

        # Define the mapping of digits to letters
        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def backtrack(combination, next_digits):
            # If there are no more digits to check, add the combination to the list
            if not next_digits:
                combinations.append(combination)
            else:
                # Iterate through the letters corresponding to the next digit
                for letter in mapping[next_digits[0]]:
                    # Append the current letter to the combination and call the function recursively
                    backtrack(combination + letter, next_digits[1:])

        combinations = []
        backtrack('', digits)
        return combinations
