# Last updated: 8/4/2025, 9:16:22 PM
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(maze), len(maze[0])
        seen = set()
        
        def roll(r, c, dr, dc):
            while 0 <= r + dr < rows and 0 <= c + dc < cols and maze[r + dr][c + dc] == 0:
                r = r + dr
                c = c + dc
            return r, c
        
        def dfs(r, c):
            if [r, c] == destination:
                return True
            for dr, dc in directions:
                nr, nc = roll(r, c, dr, dc)
                if (nr, nc) not in seen:
                    seen.add((nr, nc))
                    if dfs(nr, nc):
                        return True
            return False
        
        seen.add((start[0], start[1]))
        return dfs(start[0], start[1])