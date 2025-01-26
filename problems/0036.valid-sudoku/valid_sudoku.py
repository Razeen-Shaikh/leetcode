from ast import List


class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        Note:

        A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        Only the filled cells need to be validated according to the mentioned rules.

        Args:
        board (List[List[str]]): A 9x9 grid representing the Sudoku board.

        Returns:
        bool: True if the board is valid, False otherwise.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                
                if num == ".":
                    continue
                
                box_index = (row // 3) * 3 + (col // 3)

                if num in rows[row]:
                    return False
                if num in cols[col]:
                    return False
                if num in boxes[box_index]:
                    return False

                rows[row].add(num)
                cols[col].add(num)
                boxes[box_index].add(num)

        return True