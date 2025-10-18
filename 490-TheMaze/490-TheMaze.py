# Last updated: 10/18/2025, 11:57:21 AM
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = set()

        def roll(r, c, dr, dc):
            nr, nc = r, c
            while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] != 1:
                nr, nc = nr + dr, nc + dc
            return nr, nc

        def dfs(r, c):
            if (r, c) in seen:
                return False
            if (r, c) == (destination[0], destination[1]):
                return True
            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = roll(r, c, dr, dc)
                if dfs(nr, nc):
                    return True
            return False

        return dfs(start[0], start[1])