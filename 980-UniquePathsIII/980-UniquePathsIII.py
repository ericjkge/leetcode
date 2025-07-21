# Last updated: 7/21/2025, 1:49:43 PM
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        obstacles = ans = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        start = (0, 0)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == -1:
                    obstacles += 1
                if grid[r][c] == 1:
                    start = (r, c)
        
        total = rows * cols - obstacles # -1 for start

        def backtrack(used, path):
            nonlocal ans
            if len(path) == total:
                ans += 1
                return
            
            r, c = path[-1]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= rows or nr < 0 or nc >= cols or nc < 0 or (nr, nc) in used or (grid[nr][nc] == 2 and len(path) != total - 1) or grid[nr][nc] == -1:
                    continue
                path.append((nr, nc))
                used.add((nr, nc))
                backtrack(used, path)
                path.pop()
                used.remove((nr, nc))
            
        backtrack({start}, [start])
        return ans