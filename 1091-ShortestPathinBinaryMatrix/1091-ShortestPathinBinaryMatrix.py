# Last updated: 8/11/2025, 9:58:25 PM
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        queue = deque([(0, 0)])
        seen = set([(0, 0)])
        dist = 1
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r, c) == (rows - 1, cols - 1):
                    return dist
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] == 0:
                        seen.add((nr, nc))
                        queue.append((nr, nc))
            dist += 1
        
        return -1