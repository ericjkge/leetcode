# Last updated: 8/15/2025, 12:16:34 AM
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        @cache
        def dp(i, j):
            if i == m or j == n:
                return float("inf")
            
            if i == m - 1 and j == n - 1:
                return max(1, 1 - dungeon[i][j])
            
            nxt = min(dp(i + 1, j), dp(i, j + 1))
            return max(1, nxt - dungeon[i][j])

        return dp(0, 0)