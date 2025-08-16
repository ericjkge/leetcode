# Last updated: 8/17/2025, 12:29:55 AM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def backtrack(r, c, index):
            if index == n - 1:
                return board[r][c] == word[index]
            if board[r][c] != word[index]:
                return False
            
            original = board[r][c]
            board[r][c] = "#"
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols) or board[nr][nc] == "#":
                    continue
                if backtrack(nr, nc, index + 1):
                    return True
            board[r][c] = original
            return False
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False

# Time: O(n * m * 3^w)
# Space: O(w)