# Last updated: 7/9/2025, 2:09:12 PM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        perimeter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == 0:
                            perimeter += 1
        
        return perimeter
