# Last updated: 7/21/2025, 2:00:12 PM
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total = 0
        start = None
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != -1:
                    total += 1
                if grid[r][c] == 1:
                    start = (r, c)
        
        ans = 0
        def backtrack(r, c, used):
            nonlocal ans
            if len(used) == total:
                ans += 1
                return
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) in used or (grid[nr][nc] == 2 and len(used) != total - 1) or grid[nr][nc] == -1:
                    continue
                used.add((nr, nc))
                backtrack(nr, nc, used)
                used.remove((nr, nc))
            
        backtrack(start[0], start[1], {start})
        return ans