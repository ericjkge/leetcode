# Last updated: 7/9/2025, 2:40:16 PM
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()

        def dfs(node, counter):
            enclosed = True
            r, c = node
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    enclosed = False
                    continue
                if grid[nr][nc] == 1 and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    counter[0] += 1
                    if not dfs((nr, nc), counter):
                        enclosed = False
            return enclosed

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                counter = [1]
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    if dfs((i, j), counter):
                        ans += counter[0]
        
        return ans
        
