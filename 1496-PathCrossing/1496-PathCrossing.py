# Last updated: 7/4/2025, 10:23:03 AM
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        seen = {(0, 0)}
        directions = {
            "N":(0, 1),
            "S":(0, -1),
            "E":(1, 0),
            "W":(-1, 0)
        }

        for p in path:
            dx, dy = directions[p]
            x, y = x + dx, y + dy
            if (x, y) in seen:
                return True
            seen.add((x, y))

        return False