# Last updated: 6/7/2025, 11:12:21 AM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        time = fresh = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append([i, j])
        
        while queue and fresh > 0:
            for i in range(len(queue)): # Epoch
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append([nx, ny])
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1