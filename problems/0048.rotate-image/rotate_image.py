"""Module to rotate an image by 90 degrees."""
from typing import List

class Solution:
    """Class to rotate an image by 90 degrees."""
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the input matrix by 90 degrees in place.

        Args:
            matrix (List[List[int]]): The input matrix to be rotated.

        Returns:
            None
        """
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row of the transposed matrix
        for i in range(n):
            matrix[i].reverse()
