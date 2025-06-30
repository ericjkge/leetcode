# Last updated: 6/30/2025, 12:13:47 AM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i] or (r, c) in path):
                return False
            
            path.add((r, c))
            for dx, dy in directions:
                if backtrack(r + dx, c + dy, i + 1):
                    return True
            path.remove((r, c))
            return False

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        return False