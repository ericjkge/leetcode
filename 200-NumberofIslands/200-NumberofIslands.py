# Last updated: 6/28/2025, 6:02:02 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
        counter = 0

        def dfs(node):
            stack = [node]
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1' and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        stack.append([nx, ny])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == '1':
                    seen.add((i, j))
                    counter += 1
                    dfs([i, j])
        return counter