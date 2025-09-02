# Last updated: 9/1/2025, 9:00:29 PM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()

        def backtrack(r, c, index):
            if index == n - 1:
                return board[r][c] == word[index]

            if board[r][c] != word[index]:
                return False

            seen.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen:
                    if backtrack(nr, nc, index + 1):
                        return True

            seen.remove((r, c))
        
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        return False