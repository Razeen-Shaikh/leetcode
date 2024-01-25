"""ZigZag Conversion"""

class Solution:
    """
    This class provides methods for converting the input string
    into a zigzag pattern with a specified number of rows.
    """
    def convert(self, s: str, num_rows: int) -> str:
        """
        Convert the input string `s` into a zigzag pattern with `num_rows` rows.

        Args:
            s (str): The input string to be converted.
            num_rows (int): The number of rows in the zigzag pattern.

        Returns:
            str: The string after conversion into a zigzag pattern.
        """
        if num_rows == 1 or num_rows >= len(s):
            return s

        result = [''] * num_rows
        index, step = 0, 1

        for char in s:
            result[index] += char

            if index == 0:
                step = 1
            elif index == num_rows - 1:
                step = -1

            index += step

        return ''.join(result)
