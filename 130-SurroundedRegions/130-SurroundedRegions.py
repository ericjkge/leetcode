# Last updated: 10/19/2025, 9:36:05 AM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = set()
        regions = []

        def dfs(r, c):
            region.append((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and board[nr][nc] == "O":
                    seen.add((nr, nc))
                    dfs(nr, nc)
        
        for r in range(m):
            for c in range(n):
                if (r, c) not in seen and board[r][c] == "O":
                    region = []
                    seen.add((r, c))
                    dfs(r, c)
                    regions.append(region)
        
        for region in regions:
            if any(r < 1 or r >= m - 1 or c < 1 or c >= n - 1 for r, c in region):
                continue
            
            for r, c in region:
                board[r][c] = "X"