# Last updated: 11/9/2025, 10:09:13 PM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        seen = set()

        # Validate rows
        for row in range(rows):
            seen = set()
            for col in range(cols):
                if board[row][col] in seen and board[row][col].isalnum():
                    return False
                seen.add(board[row][col])


        # Validate cols
        for col in range(cols):
            seen = set()
            for row in range(rows):
                if board[row][col] in seen and board[row][col].isalnum():
                    return False
                seen.add(board[row][col])
        
        # Validate sub-boxes
        for row in range(0, rows, 3):
            for col in range(0, cols, 3):
                seen = set()
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] in seen and board[r][c].isalnum():
                            return False
                        seen.add(board[r][c])
        
        return True