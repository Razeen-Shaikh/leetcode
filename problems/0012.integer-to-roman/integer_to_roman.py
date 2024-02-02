"""
Module for converting integers to Roman numerals.
"""

class Solution:
    """
    Class for converting an integer to a Roman numeral.
    """
    def int_to_roman(self, num: int) -> str:
        """
        Convert an integer to a Roman numeral.
        
        Args:
            num (int): The input integer to be converted.
        
        Returns:
            str: The Roman numeral representation of the input integer.
        """
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
