# Last updated: 11/14/2025, 10:17:21 AM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] == "1":
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == "1":
                    ans += 1
                    dfs(r, c)
        
        return ans