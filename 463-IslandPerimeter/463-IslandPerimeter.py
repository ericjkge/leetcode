# Last updated: 7/9/2025, 1:23:44 PM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        stack = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        perimeter = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    stack.append((i, j))
                    seen.add((i, j))
                    break
        
        while stack:
            r, c = stack.pop()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == 0:
                    perimeter += 1
                elif (nr, nc) not in seen:
                    seen.add((nr, nc))
                    stack.append((nr, nc))
        
        return perimeter
