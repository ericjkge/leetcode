# Last updated: 7/20/2025, 3:29:47 PM
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def dfs(node, time):
            r, c = node
            if r == n - 1 and c == n - 1:
                return True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= time and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    if dfs((nr, nc), time):
                        return True
            return False
        
        left, right = 0, max(max(row) for row in grid)
        while left < right:
            seen = set()
            mid = left + (right - left) // 2
            if grid[0][0] <= mid and dfs((0, 0), mid):
                right = mid
            else:
                left = mid + 1
        return left