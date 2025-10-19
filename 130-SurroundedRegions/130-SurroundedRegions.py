# Last updated: 10/19/2025, 9:41:40 AM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = set()

        def dfs(r, c):
            board[r][c] = "S"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and board[nr][nc] == "O":
                    seen.add((nr, nc))
                    dfs(nr, nc)
        
        for r in range(m):
            if board[r][0] == "O":
                seen.add((r, 0))
                dfs(r, 0)
            if board[r][n - 1] == "O":
                seen.add((r, n - 1))
                dfs(r, n - 1)

        for c in range(n):
            if board[0][c] == "O":
                seen.add((0, c))
                dfs(0, c)
            if board[m - 1][c] == "O":
                seen.add((m - 1, c))
                dfs(m - 1, c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"