# Last updated: 7/4/2025, 10:21:58 AM
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = (0, 0)
        seen = set()
        seen.add((0, 0))
        directions = {
            "N":(0, 1),
            "S":(0, -1),
            "E":(1, 0),
            "W":(-1, 0)
        }

        for p in path:
            x, y = pos
            dx, dy = directions[p]
            nx, ny = x + dx, y + dy
            pos = (nx, ny)
            if (nx, ny) in seen:
                return True
            seen.add((nx, ny))

        return False