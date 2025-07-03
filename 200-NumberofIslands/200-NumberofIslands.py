# Last updated: 7/3/2025, 12:55:38 AM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        counter = 0
        seen = set()

        def dfs(x, y):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in seen and grid[nx][ny] == "1":
                    seen.add((nx, ny))
                    dfs(nx, ny)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == "1":
                    counter += 1
                    dfs(i, j)
        
        return counter
