"""
Module for solving Sudoku problems.
"""

from ast import List


class Solution:
    """
    This class is for solving a specific problem.
    """
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        """
        Check if the given Sudoku board is valid.

        Args:
        board (List[List[str]]): A 9x9 grid representing the Sudoku board.

        Returns:
        bool: True if the board is valid, False otherwise.
        """
        n = 9
        for r in range(n):
            row = [c for c in board[r] if c != "."]
            if len(row) != len(set(row)):
                return False

        for c in range(n):
            col = [board[r][c] for r in range(n) if board[r][c] != "."]
            if len(col) != len(set(col)):
                return False

        def block(R, C):
            l = set()
            for r in range(R, R+3):
                for c in range(C, C+3):
                    if board[r][c] == ".":
                        continue
                    if board[r][c] not in l:
                        l.add(board[r][c])
                    else:
                        return False
            return True

        for r in range(0, n, 3):
            for c in range(0, n, 3):
                if not block(r, c):
                    return False

        return True
