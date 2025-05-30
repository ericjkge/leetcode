# Last updated: 5/30/2025, 12:07:48 PM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def isValid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col):
            area = 1
            for direction in directions:
                dx, dy = direction[0], direction[1]
                nrow, ncol = row + dx, col + dy
                if isValid(nrow, ncol) and grid[nrow][ncol] == 1 and (nrow, ncol) not in seen:
                    seen.add((nrow, ncol))
                    area += dfs(nrow, ncol)
            return area
        
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        max_area = 0
        
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    max_area = max(max_area, dfs(i, j))

        
        return max_area
                    