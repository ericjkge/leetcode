# Last updated: 11/24/2025, 12:25:32 AM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()

        def backtrack(index, r, c):
            print(board[r][c])
            if index == len(word) - 1:
                return True

            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and board[nr][nc] == word[index + 1]:
                    if backtrack(index + 1, nr, nc):
                        return True
            seen.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(0, r, c):
                        return True
        return False
