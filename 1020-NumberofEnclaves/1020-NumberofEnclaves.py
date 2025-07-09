# Last updated: 7/9/2025, 2:57:44 PM
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            grid[r][c] = 0
            for dr, dc, in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    dfs(nr, nc)
        
        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows - 1] or c in [0, cols - 1]) and grid[r][c] == 1:
                    dfs(r, c)
        
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ans += 1

        return ans
            