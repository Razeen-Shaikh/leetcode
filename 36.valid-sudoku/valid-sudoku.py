from ast import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
